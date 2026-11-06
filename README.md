# HP ZBook Fury 15 G7 Hackintosh

An OpenCore EFI snapshot and setup notes for an **HP ZBook Fury 15 G7 with an Intel Core i7-10850H**, running **macOS Sequoia 15.7.7 (24G720)**.

**OpenCore:** 1.0.8 RELEASE · **SMBIOS:** MacBookPro16,2 · **Snapshot:** 7 November 2026

[Download the release](https://github.com/vurulkan/HP-ZBook-Fury-15-G7-Hackintosh/releases/latest) · [Türkçe](README.tr.md) · [Setup guide](docs/SETUP.md) · [Configuration notes](docs/CONFIGURATION.md) · [Blog](https://blog.vurulkan.com/posts/hp-zbook-fury-15-g7-hackintosh/)

This is a snapshot of a boot-tested personal configuration, with machine identity and saved Wi-Fi credentials removed. **Generate your own SMBIOS identity before booting it.** The blank identity in the download is intentional.

The Fury G7 was sold with different GPUs, panels, wireless cards and firmware revisions. A matching model name alone does not establish compatibility. Keep your existing EFI and test this configuration from a USB drive first.

## Hardware

| Component | Tested configuration |
| --- | --- |
| Laptop | HP ZBook Fury 15 G7 |
| CPU | Intel Core i7-10850H, Comet Lake-H, 6 cores / 12 threads |
| Graphics | Intel UHD Graphics 630; device ID presented to macOS as `0x3E9B` |
| Internal display | 1920 × 1080, 60 Hz |
| RAM | 32 GB DDR4; macOS reports 2133 MHz |
| macOS SSD | WDC PC SN730, 512 GB, NVMe; TRIM enabled |
| Wireless | Intel Wi-Fi using itlwm + HeliPort; exact module model not independently recorded |
| Bluetooth | Intel firmware stack + BlueToolFixup |
| Ethernet | Intel, IntelMausi driver included; cable connectivity not verified in this audit |
| Audio | AppleALC with `alcid=66`; exact codec not independently identified |
| Power supply used during tests | 150 W AC adapter |
| Firmware in Windows test | HP S92 01.25.00 |

The discrete GPU is excluded from macOS by `-wegnoegpu`. Its exact SKU and external-display routing are not documented here.

## Verified features and remaining work

| Feature | Status / evidence |
| --- | --- |
| Booting macOS 15.7.7 | Verified after OpenCore and kext updates |
| Intel graphics acceleration | Metal 3 reported; internal display active |
| Brightness slider | Confirmed working |
| Fn+F3 / Fn+F4 brightness | Confirmed working after the HP ACPI event fix |
| Fn volume controls | Confirmed working |
| Wi-Fi | Working with itlwm 2.3.0 + HeliPort |
| Bluetooth | Confirmed working by the machine owner |
| Audio | Built-in input/output devices detected; volume controls work. Recording and jack tests remain open |
| Battery reporting | Driver active and capacity/cycle information available |
| CPU power management | CPUFriend and X86PlatformPlugin active; sustained-load limitation remains, see below |
| Software Update discovery | Fixed and verified: Sequoia 15.8.2 is offered with RestrictEvents |
| Location Services / Find My | Not working with the current itlwm configuration |
| Keyboard / pointing devices | Drivers included; a complete gesture/TrackPoint test matrix has not been performed |
| USB ports | Existing maps retained; each physical port has not been retested |
| Sleep / wake / hibernation | ACPI and drivers included; complete physical testing remains open |
| Camera, HDMI, DisplayPort, Thunderbolt, docks, card reader | Not verified in this audit |
| FileVault, AirDrop, iMessage / FaceTime | Not verified |

**15.8.2 is discoverable, not yet installation-tested.** Tahoe 26.7.2 also appears in Software Update; that is not a compatibility claim or an upgrade recommendation.

### Known limitations

- **Location:** itlwm exposes the wireless adapter as Ethernet, so the Wi-Fi information needed by Location Services is unavailable. HeliPort autostart does not change this. Choose your time zone manually; automatic clock synchronization and automatic time-zone selection are separate settings.
- **Sustained CPU load:** this machine settles near 25 W and 2.75 GHz in the recorded macOS workload. Windows sustained a higher clock/power level in a different workload. These are not directly comparable benchmark scores and do not establish a performance-loss percentage. Changing CPUFriend vectors or trying MacBookPro16,1 did not resolve it; those experiments were reverted.
- **Configuration debt:** multiple EC/USBX SSDTs, both USBMap and UTBMap, and the existing legacy wireless stack are preserved. They have not been independently simplified or validated on every port. One inherited sleep rename has identical Find/Replace bytes and is a no-op. See [configuration notes](docs/CONFIGURATION.md).
- **Security settings:** this snapshot has customized, disabled SIP (`FF0F0000`), `SecureBootModel=Disabled`, and AMFIPass present. These are disclosed existing settings, not instructions to disable protections on an unrelated installation. Existing legacy networking/root-patch dependencies require separate review.

## Download and prepare

1. Download the EFI ZIP and `SHA256SUMS.txt` from the [latest release](https://github.com/vurulkan/HP-ZBook-Fury-15-G7-Hackintosh/releases/latest).
2. Verify the archive before editing it: `shasum -a 256 -c SHA256SUMS.txt` from the download directory.
3. Extract it and read [SETUP.md](docs/SETUP.md). Generate **MacBookPro16,2** values with [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS): populate `SystemSerialNumber`, `MLB`, `SystemUUID` and a suitable six-byte `ROM` in `EFI/OC/config.plist`.
4. Validate the edited config with **ocvalidate from OpenCore 1.0.8**.
5. Copy the `EFI` directory to a USB EFI partition and boot it for testing. Retain a bootable backup of your own configuration.
6. Install [HeliPort](https://github.com/OpenIntelWireless/HeliPort/releases) separately and add it to Login Items if desired. HeliPort is a macOS application, not an EFI component.

The release contains EFI files only plus documentation, notices and the brightness SSDT source. It contains no macOS installer, Apple account data, diagnostics, benchmark dumps or register-access tools.

## Main components

| Component | Version |
| --- | --- |
| OpenCore | 1.0.8 RELEASE |
| Lilu | 1.7.2 |
| WhateverGreen | 1.7.1 |
| VirtualSMC / battery and sensor plugins | 1.3.8 |
| AppleALC | 1.9.8 |
| RestrictEvents | 1.1.6 |
| Intel Wi-Fi: itlwm | 2.3.0 |
| IntelBluetoothFirmware / IntelBTPatcher | 2.5.0 |
| BlueToolFixup | 2.7.2 |
| VoodooPS2Controller | 2.3.8 |
| VoodooRMI / VoodooSMBus | 1.4.3 / 3.0 |
| VoodooI2C | 2.9.1 |
| USBToolBox | 1.2.0 |
| BrightnessKeys | 1.0.4 |
| CPUFriend | 1.3.0 |

The [complete inventory](docs/KEXTS.md) records enabled and disabled config entries, plugins and version ranges. A bundled version number does not always correspond to an upstream stable release: some inherited Intel/networking components are rolling builds.

## Brightness fix

The HP firmware dispatches brightness events `0x86` and `0x87` through `\_GPE.G001`. The original route did not reach the device handled by BrightnessKeys.

This configuration renames the original method definition to `Z001` and supplies a wrapper in [SSDT-HP-Brightness.dsl](Sources/ACPI/SSDT-HP-Brightness.dsl). On Darwin, the two brightness events notify `\_SB.PCI0.GFX0.DD02`. Other events and operating systems call the original method.

The rename is constrained to the audited DSDT: signature `DSDT`, OEM table ID `8783    `, length 184887 bytes, one match. Firmware changes can invalidate those assumptions. Full patch details are in [CONFIGURATION.md](docs/CONFIGURATION.md#hp-brightness-keys).

## Software updates

RestrictEvents 1.1.6 is enabled with:

```text
revpatch=sbvmm revblock=none
```

`sbvmm` changes the Secure Boot model used by update eligibility checks to the VMM model. `revblock=none` leaves its process-blocking features off. After reboot, `softwareupdate --list` changed from “No new software available” to listing Sequoia 15.8.2 and Tahoe 26.7.2. No OS update was installed as part of that verification.

Review the existing legacy wireless/root-patch setup before installing any OS update. Discovery alone does not validate a successful upgrade or post-update networking.

## Repository layout

```text
EFI/                   Sanitized boot configuration and binaries
Sources/ACPI/          Source of the custom HP brightness wrapper
docs/                  Setup, limitations, configuration and inventories
licenses/              Available upstream license texts
scripts/               Public-package checks and release builder
.github/workflows/     Automated sanitized-config validation
```

For a public-copy check, run `python3 scripts/validate.py`. To also run OpenCore's validator, use `python3 scripts/validate.py --ocvalidate /path/to/1.0.8/ocvalidate`. This public-copy check intentionally rejects a personalized config.

## Credits and licensing

Thanks to Acidanthera, OpenIntelWireless, Voodoo driver contributors, USBToolBox, Dortania and the other upstream authors listed in [THIRD_PARTY.md](THIRD_PARTY.md).

Original documentation and publication scripts are covered by [LICENSE](LICENSE). Third-party binaries, inherited SSDTs and Apple components retain their respective ownership and licenses; the repository license does not relicense them.
