# Recorded CPU behavior

These are observations from one laptop and a troubleshooting session, not a standardized cross-platform benchmark.

| Condition | Observation |
| --- | --- |
| Hardware / supply | i7-10850H, 150 W adapter |
| macOS sustained workload | Approximately 25 W package power, 2.75 GHz |
| macOS brief peaks | Approximately 85 W and 98–99 °C during initial turbo |
| macOS single-worker clock | Approximately 4.62 GHz |
| Windows longer-load observation | Final sampled clock approximately 3.59 GHz; power declined across rounds from roughly 66 W to 45 W |
| BIOS Intel Dynamic Tuning | Disabled before the recorded Windows test and following macOS comparison |
| Read-only package-limit observation | MSR 0x610 decoded to PL1 85 W / PL2 125 W under both OSes; macOS's sustained 25 W was not encoded there as a 25 W PL1 |

The macOS workload used LibreSSL/OpenSSL SHA-256 workers. The Windows tool used a different implementation. Clock, power and temperature readings are useful diagnostics, but the workloads do not support a numerical claim that macOS is a given percentage slower than Windows.

Changing CPUFriend vectors and trying MacBookPro16,1 did not resolve the behavior. Those trials were reverted. Disabling Intel Dynamic Tuning in BIOS did not remove the observed macOS behavior either. The controlling mechanism remains unresolved; firmware, other power-control paths and OS policy were not conclusively separated.

Temporary diagnostic components were removed from EFI and confirmed unloaded after reboot. They are not distributed here. This release does not change CPU voltage or power-limit registers.
