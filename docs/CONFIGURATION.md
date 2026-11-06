# Configuration notes

## Snapshot and sanitization

Captured on 7 November 2026 from the boot-tested OpenCore 1.0.8 installation. The live EFI is not modified by the publication process.

Public-copy changes are limited to:

- Empty `PlatformInfo/Generic/SystemSerialNumber`, `MLB` and `SystemUUID`.
- Zero the six bytes of `PlatformInfo/Generic/ROM`.
- Remove `bluetoothInternalControllerInfo` and `bluetoothExternalDongleFailed` from NVRAM Add; they are captured local controller state.
- Empty itlwm's `WiFiConfig` so no preconfigured SSID or password is distributed.
- Exclude `oldConfig.plist`, backup/log/debug-symbol files and Finder metadata.

No macOS preferences, HeliPort credentials, raw DSDT dumps, performance captures or diagnostic drivers are published. OpenCore namespace GUIDs, PCI IDs and ACPI table IDs are configuration identifiers, not the removed personal SystemUUID.

## Boot arguments

```text
-v keepsyms=1 debug=0x100 -wegnoegpu alcid=66 -igfxblt revpatch=sbvmm revblock=none
```

| Argument | Purpose in this snapshot |
| --- | --- |
| `-v` | Verbose boot |
| `keepsyms=1 debug=0x100` | Retained diagnostic boot settings |
| `-wegnoegpu` | Exclude external/discrete GPUs from macOS through WhateverGreen |
| `alcid=66` | AppleALC audio layout selection |
| `-igfxblt` | Retained WhateverGreen backlight-related setting |
| `revpatch=sbvmm` | RestrictEvents update eligibility patch using the VMM Secure Boot model |
| `revblock=none` | Disable RestrictEvents process-blocking features |

## HP brightness keys

Firmware ACPI events `_Q86` and `_Q87` call `\_GPE.G001` with brightness event codes `0x86` and `0x87`. The original implementation eventually notified `DD1F`; the working BrightnessKeys path is `\_SB.PCI0.GFX0.DD02`.

The added SSDT wraps the event dispatcher. On Darwin it sends those two events to `DD02`; otherwise it calls the original, renamed `Z001` method. The owner confirmed Fn+F3/F4 work after reboot.

The ACPI Patch entry is constrained as follows:

| Field | Value |
| --- | --- |
| Table signature | `DSDT` |
| OEM Table ID | `8783    ` (four trailing spaces) |
| Table length | 184887 |
| Count | 1 |
| Find | `14 49 15 47 30 30 31 09` |
| Replace | `14 49 15 5A 30 30 31 09` |

Only the matching method definition is renamed, rather than blindly renaming every occurrence of `G001`. The [DSL source](../Sources/ACPI/SSDT-HP-Brightness.dsl) is included. After a firmware change, recheck the DSDT and method signature before reusing this patch.

## CPUFriend and SMBIOS

The retained model is **MacBookPro16,2**. CPUFriendDataProvider is loaded after CPUFriend. Its frequency-vector payload was inherited from the original configuration and matches the audited MacBookAir9,1 stock vectors. That describes the provider data's origin; it does not mean that the advertised machine model is a MacBook Air.

Trials with MacBookPro16,1 power-management data and then the MacBookPro16,1 model did not improve sustained throughput. They were reverted. The public EFI contains the restored MacBookPro16,2 configuration and original provider payload, not an experimental performance profile.

See [PERFORMANCE.md](PERFORMANCE.md) for the measurements and their limitations. There is no VoltageShift kext, MSR writer, undervolting profile or scheduled power-limit task in this release.

## Networking and USB

itlwm 2.3.0 handles Intel Wi-Fi, with HeliPort installed separately. Bluetooth uses IntelBluetoothFirmware, IntelBTPatcher and BlueToolFixup.

The inherited configuration also contains IOSkywalkFamily, IO80211FamilyLegacy/AirPortBrcmNIC and AMFIPass. Their presence is not a claim that Intel Wi-Fi requires the whole legacy stack. They were retained because the existing installation may have OS-side root-patch dependencies that were not reconstructed during this audit. Treat this release as an exact configuration snapshot, not a minimal fresh-install recipe.

USBMap and USBToolBox/UTBMap are both enabled and retain the MacBookPro16,2 matching. Their coexistence is disclosed; it has not been proven necessary. Validate physical ports and controller matching before adapting the maps.

## Existing settings and unresolved items

| Setting / item | Recorded state |
| --- | --- |
| SIP `csr-active-config` | Data `FF0F0000`, customized disabled configuration |
| `Misc/Security/SecureBootModel` | `Disabled` |
| `Misc/Security/Vault` | `Optional` |
| `Misc/Security/DmgLoading` | `Signed` |
| `Kernel/Quirks/DisableIoMapper` | `True` |
| `Kernel/Quirks/AppleXcpmCfgLock` | `True` |
| `Kernel/Quirks/XhciPortLimit` | `False` |
| Multiple EC/USBX SSDTs | Present; independent namespace simplification not completed |
| Inherited `_S0 to XS0` rename | Find and Replace are identical; it performs no change |
| Thunderbolt | An older IOThunderboltFamily panic was observed; cause and physical operation remain unverified |

No additional protection was disabled to prepare this publication. Existing settings must be reviewed against the actual installed macOS patches before changing them or transplanting the EFI.

## ACPI inventory

All nineteen enabled ACPI Add entries are recorded in [acpi-inventory.json](acpi-inventory.json). Names indicate intended roles; their presence is not proof of successful hardware testing:

- AWAC, EC/USBX and PMC tables: retained platform/timer/power scaffolding.
- GPU-SPOOF, PNLF and HP-Brightness: integrated-display identification/backlight handling and the verified brightness wrapper.
- PLUG-DRTNIA: retained CPU plugin attachment.
- GPIO, HPET, GPRW and XOSI: retained device, IRQ and OS-identity adjustments.
- HP-FixLidSleep, PTSWAKTTS, DeepIdle and PCI0.LPCB-Wake-AOAC: retained sleep/wake-related tables; full suspend/resume testing remains open.
- TB3-HP and DMAR: retained Thunderbolt/IOMMU-related tables; no new Thunderbolt compatibility claim is made.

Only the new brightness wrapper source is provided as an audited source in `Sources/ACPI`. Existing AML files are not presented as newly authored or universally portable.
