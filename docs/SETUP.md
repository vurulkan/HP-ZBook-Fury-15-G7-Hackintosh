# Setup and recovery

## Scope

This release targets the hardware and firmware listed in the root README. It was captured from macOS **15.7.7**, not from an updated 15.8.2 installation. Do not interpret an update offered by Software Update as proof that every driver will survive that upgrade.

## Before replacing an EFI

- Back up the EFI you already boot with and keep a USB recovery path.
- Compare your CPU, panel, wireless hardware, SSDs and BIOS version with the recorded configuration.
- Check the firmware-dependent brightness rename and the machine-specific USB maps.
- Record your current BIOS settings. A complete BIOS preset was not captured, so this repository does not present guessed settings as tested facts.
- Intel Dynamic Tuning was disabled in BIOS during the last Windows/macOS comparison. It did **not** remove the observed macOS sustained-power behavior. No universal recommendation to disable it is made.

## 1. Verify the download

Put the release ZIP and `SHA256SUMS.txt` in the same directory, then run:

```sh
shasum -a 256 -c SHA256SUMS.txt
```

Verify before changing anything. `EFI-SHA256SUMS.txt`, included inside the archive, records individual sanitized EFI file hashes. After filling in your identity, the hash of `config.plist` will intentionally differ.

## 2. Create your own identity

Use [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) to generate an identity for **MacBookPro16,2** and edit `EFI/OC/config.plist`:

| Key under `PlatformInfo/Generic` | Public release | Required action |
| --- | --- | --- |
| `SystemProductName` | `MacBookPro16,2` | Keep for this configuration |
| `SystemSerialNumber` | Empty string | Supply your generated serial |
| `MLB` | Empty string | Supply the matching generated board serial |
| `SystemUUID` | Empty string | Supply your generated UUID |
| `ROM` | Six zero bytes, plist Data type | Supply your own suitable six-byte value and preserve Data type |

Do not copy another person's serial/MLB/UUID or publish your personalized config. Do not substitute an ASCII MAC-address string into the Data field. USB map personalities and CPU power-management choices are tied to the current configuration; changing the SMBIOS is more than changing a display label.

The public repository validator rejects populated identity fields on purpose. Once personalized, use OpenCore's `ocvalidate` to validate your working copy rather than trying to make it pass the public-privacy check.

## 3. Validate

Download the [OpenCore 1.0.8 RELEASE package](https://github.com/acidanthera/OpenCorePkg/releases/tag/1.0.8), then run its matching validator:

```sh
/path/to/OpenCore-1.0.8-RELEASE/Utilities/ocvalidate/ocvalidate /path/to/EFI/OC/config.plist
```

A clean result verifies config structure and supported settings. It does not prove that an SSDT, USB map or graphics path matches your laptop.

## 4. Test from USB

Copy the extracted **EFI directory** to the root of your USB drive's EFI partition. Confirm the resulting paths are `EFI/BOOT/BOOTx64.efi` and `EFI/OC/config.plist`, rather than `EFI/EFI/...`.

Choose that USB's UEFI entry from the HP boot menu and test:

- Normal boot, graphics acceleration and the internal display.
- Brightness slider, Fn+F3/F4 and Fn volume controls.
- Wi-Fi through HeliPort, Bluetooth and audio.
- Each physical USB port, including USB 2 and USB 3 devices where applicable.
- Sleep/wake on battery and AC, lid close/open, camera and external displays.

Move it to your internal EFI only after the functions you need work. Do not overwrite the whole partition: preserve unrelated Windows or other bootloader directories.

## 5. HeliPort, location and time

Install [HeliPort](https://github.com/OpenIntelWireless/HeliPort/releases) in Applications. To launch it at login, add it in **System Settings → General → Login Items**. The application and its saved networks are not bundled here.

itlwm presents an Ethernet interface; this limits native Wi-Fi-dependent location functionality. Select your desired time zone manually in **System Settings → General → Date & Time** if automatic selection fails. Keep automatic date/time synchronization configured separately. `Europe/Istanbul` is the time zone used on the audited machine, not an EFI setting.

If clock errors occur specifically after switching between Windows and macOS, investigate the dual-boot RTC convention separately. This package does not change Windows registry settings or install a clock-fix service.

## 6. Software Update

The current config includes RestrictEvents 1.1.6 with `revpatch=sbvmm revblock=none`. After booting it, you can inspect without installing:

```sh
sysctl -n kern.bootargs
kmutil showloaded | grep RestrictEvents
softwareupdate --list
```

The audit verified that Sequoia 15.8.2 becomes visible. Stay within the tested Sequoia scope until a separate upgrade test is available. Inspect the legacy networking/root-patch dependencies before applying an update; this EFI alone is not a full record of files patched on the macOS system volume.

## Recovery

If the USB does not boot correctly, select your previous bootable EFI. If you already copied it internally, boot your recovery USB and restore **your own** saved EFI. This repository does not require an NVRAM reset, firmware flash, security bypass during recovery or register writes.

When reporting an issue, provide hardware/BIOS versions, macOS build, the release tag and the failing feature. Redact serials, UUIDs, MLB, ROM/MAC addresses, saved networks and account data before attaching any config or log.
