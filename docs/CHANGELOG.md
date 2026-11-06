# Changelog

## v1.0.0 — 2026-11-07

First public, sanitized snapshot for HP ZBook Fury 15 G7 / i7-10850H.

- OpenCore upgraded from 1.0.5 to 1.0.8 RELEASE, with matching drivers/tools and HideVerbose driver fields.
- Updated Lilu, WhateverGreen, VirtualSMC and sensor plugins, AppleALC, BlueToolFixup, USBToolBox, VoodooRMI and VoodooSMBus to the versions in the inventory.
- Added the firmware-specific HP brightness dispatcher wrapper; Fn+F3/F4 verified after reboot.
- Corrected CPUFriendDataProvider ordering after CPUFriend; retained the restored MacBookPro16,2 setup.
- Added RestrictEvents 1.1.6 with `revpatch=sbvmm revblock=none`; Sequoia 15.8.2 discovery verified after reboot.
- Removed public-copy SMBIOS identity, ROM, Bluetooth controller state and embedded Wi-Fi configuration.
- Added setup notes, explicit hardware/test limitations, source for the brightness wrapper, inventories and public-package validation.

Runtime tested on macOS Sequoia 15.7.7 (24G720). No successful 15.8.2 or Tahoe upgrade is claimed.
