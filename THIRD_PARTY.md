# Third-party components and notices

The repository MIT license covers original documentation and publication scripts only. It does not cover the entire EFI tree. Third-party authors retain ownership; consult the linked projects and bundled notices for their terms.

Upstream license texts available at publication time are copied into `licenses/` as reference notices. Some inherited binaries are rolling builds and their precise original source commit was not recorded. These notices do not establish new redistribution rights or relicense those binaries.

| Project / included component | Upstream | License notice |
| --- | --- | --- |
| OpenCorePkg | [acidanthera/OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) | [Text](licenses/OpenCorePkg.txt) |
| Lilu | [acidanthera/Lilu](https://github.com/acidanthera/Lilu) | [Text](licenses/Lilu.txt) |
| WhateverGreen | [acidanthera/WhateverGreen](https://github.com/acidanthera/WhateverGreen) | [Text](licenses/WhateverGreen.txt) |
| VirtualSMC | [acidanthera/VirtualSMC](https://github.com/acidanthera/VirtualSMC) | [Text](licenses/VirtualSMC.txt) |
| AppleALC | [acidanthera/AppleALC](https://github.com/acidanthera/AppleALC) | [Text](licenses/AppleALC.txt) |
| RestrictEvents | [acidanthera/RestrictEvents](https://github.com/acidanthera/RestrictEvents) | [Text](licenses/RestrictEvents.txt) |
| CPUFriend | [acidanthera/CPUFriend](https://github.com/acidanthera/CPUFriend) | [Text](licenses/CPUFriend.txt) |
| NVMeFix | [acidanthera/NVMeFix](https://github.com/acidanthera/NVMeFix) | [Text](licenses/NVMeFix.txt) |
| RTCMemoryFixup | [acidanthera/RTCMemoryFixup](https://github.com/acidanthera/RTCMemoryFixup) | [Text](licenses/RTCMemoryFixup.txt) |
| IntelMausi | [acidanthera/IntelMausi](https://github.com/acidanthera/IntelMausi) | [Text](licenses/IntelMausi.txt) |
| CpuTscSync | [acidanthera/CpuTscSync](https://github.com/acidanthera/CpuTscSync) | [Text](licenses/CpuTscSync.txt) |
| HibernationFixup | [acidanthera/HibernationFixup](https://github.com/acidanthera/HibernationFixup) | [Text](licenses/HibernationFixup.txt) |
| BlueToolFixup | [acidanthera/BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM) | [Text](licenses/BlueToolFixup.txt) |
| itlwm | [OpenIntelWireless/itlwm](https://github.com/OpenIntelWireless/itlwm) | [Text](licenses/itlwm.txt) |
| IntelBluetoothFirmware | [OpenIntelWireless/IntelBluetoothFirmware](https://github.com/OpenIntelWireless/IntelBluetoothFirmware) | [Text](licenses/IntelBluetoothFirmware.txt) |
| BrightnessKeys | [acidanthera/BrightnessKeys](https://github.com/acidanthera/BrightnessKeys) | [Text](licenses/BrightnessKeys.txt) |
| ECEnabler | [1Revenger1/ECEnabler](https://github.com/1Revenger1/ECEnabler) | Not obtained; consult upstream |
| VoodooPS2 | [acidanthera/VoodooPS2](https://github.com/acidanthera/VoodooPS2) | [Text](licenses/VoodooPS2.txt) |
| VoodooRMI | [VoodooSMBus/VoodooRMI](https://github.com/VoodooSMBus/VoodooRMI) | [Text](licenses/VoodooRMI.txt) |
| VoodooSMBus | [VoodooSMBus/VoodooSMBus](https://github.com/VoodooSMBus/VoodooSMBus) | [Text](licenses/VoodooSMBus.txt) |
| VoodooI2C | [VoodooI2C/VoodooI2C](https://github.com/VoodooI2C/VoodooI2C) | [Text](licenses/VoodooI2C.txt) |
| USBToolBox | [USBToolBox/kext](https://github.com/USBToolBox/kext) | Not obtained; consult upstream |
| AMFIPass | [dhinakg/AMFIPass](https://github.com/dhinakg/AMFIPass) | Not obtained; consult upstream |
| XHCI-unsupported | [RehabMan/OS-X-USB-Inject-All](https://github.com/RehabMan/OS-X-USB-Inject-All) | Not obtained; consult upstream |

## Apple and inherited assets

`IOSkywalkFamily.kext`, `IO80211FamilyLegacy.kext` and its `AirPortBrcmNIC.kext` plugin are inherited Apple components. They are not authored by this repository and are not MIT-licensed by it. Apple copyright notices and applicable Apple terms remain in force. Their inclusion documents the existing installation; it is not a claim that every user may redistribute them under the repository license.

HfsPlus.efi, OpenCanopy resources, pre-existing AML tables, USBMap/UTBMap personalities and CPUFriendDataProvider data were inherited from the existing EFI. Ownership and provenance vary; no new blanket license is asserted for those assets. The custom brightness wrapper source is supplied separately for review.

## Setup and background references

- [Dortania OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)
- [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS)
- [HeliPort](https://github.com/OpenIntelWireless/HeliPort)
- [itlwm Location Services limitation](https://openintelwireless.github.io/itlwm/FAQ.html#does-it-support-location-services)
- [RestrictEvents arguments and sbvmm behavior](https://github.com/acidanthera/RestrictEvents#boot-arguments)

No Apple installer, OS image, Apple account credentials, HeliPort application or register-access diagnostic tool is included.
