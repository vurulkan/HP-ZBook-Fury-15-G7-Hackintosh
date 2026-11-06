# Kext inventory

Read directly from the published `config.plist` and each referenced Info.plist. “Enabled” is the OpenCore configuration flag, not a claim that every personality attaches to hardware. Empty kernel bounds mean no bound is specified in the entry.

| Configured bundle / plugin | Bundle version | Enabled | Min kernel | Max kernel |
| --- | --- | --- | --- | --- |
| `IntelBluetoothFirmware.kext` | 2.5.0 | Yes | — | — |
| `IntelMausi.kext` | 1.0.9 | Yes | — | — |
| `IOSkywalkFamily.kext` | 1.0 | Yes | — | — |
| `itlwm.kext` | 2.3.0 | Yes | — | — |
| `Lilu.kext` | 1.7.2 | Yes | — | — |
| `NVMeFix.kext` | 1.1.3 | Yes | — | — |
| `RTCMemoryFixup.kext` | 1.0.8 | Yes | — | — |
| `USBMap.kext` | 1.0 | Yes | — | — |
| `USBToolBox.kext` | 1.2.0 | Yes | — | — |
| `UTBMap.kext` | 1.1 | Yes | — | — |
| `VirtualSMC.kext` | 1.3.8 | Yes | — | — |
| `VoodooPS2Controller.kext` | 2.3.8 | Yes | — | — |
| `VoodooRMI.kext` | 1.4.3 | Yes | — | — |
| `VoodooSMBus.kext` | 3.0 | Yes | — | — |
| `WhateverGreen.kext` | 1.7.1 | Yes | — | — |
| `XHCI-unsupported.kext` | 0.9.2 | Yes | — | — |
| `VoodooI2C.kext/Contents/PlugIns/VoodooGPIO.kext` | 1.1 | Yes | — | — |
| `VoodooI2C.kext/Contents/PlugIns/VoodooI2CServices.kext` | 1 | Yes | — | — |
| `VoodooI2C.kext/Contents/PlugIns/VoodooInput.kext` | 1.1.6 | Yes | — | — |
| `VoodooPS2Controller.kext/Contents/PlugIns/VoodooInput.kext` | 1.1.7 | No | — | — |
| `VoodooPS2Controller.kext/Contents/PlugIns/VoodooPS2Keyboard.kext` | 2.3.8 | Yes | — | — |
| `VoodooPS2Controller.kext/Contents/PlugIns/VoodooPS2Mouse.kext` | 2.3.8 | Yes | — | — |
| `VoodooPS2Controller.kext/Contents/PlugIns/VoodooPS2Trackpad.kext` | 2.3.8 | Yes | — | — |
| `VoodooRMI.kext/Contents/PlugIns/RMISMBus.kext` | 1.0 | Yes | — | — |
| `VoodooRMI.kext/Contents/PlugIns/VoodooInput.kext` | 1.1.7 | No | — | — |
| `AMFIPass.kext` | 1.4.1 | Yes | — | — |
| `AppleALC.kext` | 1.9.8 | Yes | — | — |
| `BrightnessKeys.kext` | 1.0.4 | Yes | — | — |
| `CPUFriend.kext` | 1.3.0 | Yes | — | — |
| `CPUFriendDataProvider.kext` | 1.0.1 | Yes | — | — |
| `CpuTscSync.kext` | 1.1.2 | Yes | — | — |
| `ECEnabler.kext` | 1.0.6 | Yes | — | — |
| `HibernationFixup.kext` | 1.5.4 | Yes | — | — |
| `IO80211FamilyLegacy.kext` | 1200.12.2b1 | Yes | — | — |
| `SMCBatteryManager.kext` | 1.3.8 | Yes | — | — |
| `SMCProcessor.kext` | 1.3.8 | Yes | — | — |
| `SMCSuperIO.kext` | 1.3.8 | Yes | — | — |
| `VoodooI2C.kext` | 2.9.1 | Yes | — | — |
| `VoodooI2CHID.kext` | 1 | Yes | — | — |
| `VoodooI2CSynaptics.kext` | 1 | Yes | — | — |
| `VoodooRMI.kext/Contents/PlugIns/RMII2C.kext` | 1 | Yes | — | — |
| `IO80211FamilyLegacy.kext/Contents/PlugIns/AirPortBrcmNIC.kext` | 1400.1.1 | Yes | — | — |
| `BlueToolFixup.kext` | 2.7.2 | Yes | — | — |
| `IntelBTPatcher.kext` | 2.5.0 | Yes | — | — |
| `RestrictEvents.kext` | 1.1.6 | Yes | — | — |

The snapshot also retains an unreferenced IntelBluetoothInjector.kext bundle. Bundled files and enabled Kernel/Add entries are distinct. VoodooInput copies disabled in the config are intentionally recorded as disabled, rather than being reported as simultaneous active input providers.

For the machine-readable version, see [kext-inventory.json](kext-inventory.json). For source repositories and notices, see [THIRD_PARTY.md](../THIRD_PARTY.md).
