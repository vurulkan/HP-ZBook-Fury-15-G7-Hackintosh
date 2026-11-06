#!/usr/bin/env python3
"""Validate a public EFI copy. Personalized configs intentionally fail this check."""
import argparse
import json
import pathlib
import plistlib
import subprocess
import sys


def validate(root):
    efi = root / 'EFI'
    oc = efi / 'OC'
    config = plistlib.loads((oc / 'config.plist').read_bytes())
    generic = config['PlatformInfo']['Generic']
    for key in ('SystemSerialNumber', 'MLB', 'SystemUUID'):
        if generic.get(key) != '':
            raise ValueError(f'Public copy contains populated identity field: {key}')
    if generic.get('ROM') != bytes(6):
        raise ValueError('Public ROM must be exactly six zero bytes')
    if generic.get('SystemProductName') != 'MacBookPro16,2':
        raise ValueError('Unexpected SMBIOS model for this published configuration')
    nvram = config['NVRAM']['Add']['7C436110-AB2A-4BBB-A880-FE41995C9F82']
    if any(k in nvram for k in ('bluetoothInternalControllerInfo', 'bluetoothExternalDongleFailed')):
        raise ValueError('Local Bluetooth controller state must not be published')
    args = nvram['boot-args'].split()
    if 'revpatch=sbvmm' not in args or 'revblock=none' not in args:
        raise ValueError('Expected scoped RestrictEvents configuration is missing')
    if config['Misc']['Security']['PasswordHash'] or config['Misc']['Security']['PasswordSalt']:
        raise ValueError('Do not distribute an OpenCore password hash or salt')

    count = 0
    for file in efi.rglob('*'):
        if file.is_symlink():
            raise ValueError('Unexpected symlink in EFI: ' + str(file.relative_to(root)))
        if not file.is_file():
            continue
        count += 1
        name = file.name.lower()
        if (name in ('oldconfig.plist', 'nvram.plist', '.ds_store') or
                name.startswith('._') or name.endswith(('.bak', '.log')) or
                'voltageshift' in name):
            raise ValueError('Unexpected private/diagnostic file: ' + str(file.relative_to(root)))
        if file.suffix == '.plist':
            value = plistlib.loads(file.read_bytes())
            for personality in value.get('IOKitPersonalities', {}).values():
                if personality.get('WiFiConfig'):
                    raise ValueError('Embedded Wi-Fi configuration must be empty')

    for path in ('BOOT/BOOTx64.efi', 'OC/OpenCore.efi'):
        if not (efi / path).is_file():
            raise ValueError('Missing boot file: ' + path)

    # Resolve every referenced file, including disabled entries, so the snapshot
    # cannot silently depend on files omitted from the public archive.
    def require(base, relative):
        path = (base / relative).resolve()
        if base.resolve() not in path.parents or not path.is_file():
            raise ValueError('Missing or invalid configured path: ' + relative)

    for entry in config['Kernel']['Add']:
        bundle = oc / 'Kexts' / entry['BundlePath']
        require(bundle, entry['PlistPath'])
        if entry['ExecutablePath']:
            require(bundle, entry['ExecutablePath'])
    for entry in config['ACPI']['Add']:
        require(oc / 'ACPI', entry['Path'])
    for entry in config['UEFI']['Drivers']:
        require(oc / 'Drivers', entry['Path'])
    for entry in config['Misc']['Tools']:
        require(oc / 'Tools', entry['Path'])

    enabled = [e['BundlePath'] for e in config['Kernel']['Add'] if e['Enabled']]
    if enabled.index('CPUFriend.kext') > enabled.index('CPUFriendDataProvider.kext'):
        raise ValueError('CPUFriendDataProvider must load after CPUFriend')
    if enabled.index('Lilu.kext') > enabled.index('RestrictEvents.kext'):
        raise ValueError('RestrictEvents must load after Lilu')

    # Check that the published version inventory matches the actual payload.
    expected = json.loads((root / 'docs/kext-inventory.json').read_text())
    actual = []
    for entry in config['Kernel']['Add']:
        info = plistlib.loads((oc / 'Kexts' / entry['BundlePath'] / entry['PlistPath']).read_bytes())
        actual.append(dict(bundle=entry['BundlePath'], version=info.get('CFBundleVersion', 'unknown'),
                           enabled=entry['Enabled'], min_kernel=entry['MinKernel'], max_kernel=entry['MaxKernel']))
    if actual != expected:
        raise ValueError('Kext inventory does not match EFI payload')
    print(f'Public-copy privacy, plist, inventory and configured-path checks passed ({count} EFI files).')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    parser.add_argument('--ocvalidate', type=pathlib.Path)
    options = parser.parse_args()
    try:
        validate(options.root)
        if options.ocvalidate:
            subprocess.run([str(options.ocvalidate.resolve()), str(options.root / 'EFI/OC/config.plist')], check=True)
    except (OSError, ValueError, KeyError, plistlib.InvalidFileException, subprocess.CalledProcessError) as error:
        print('Validation failed: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
