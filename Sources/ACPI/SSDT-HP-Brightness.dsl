DefinitionBlock ("", "SSDT", 2, "ZBOOK", "HPBRT", 0x00000001)
{
    External (\_GPE.Z001, MethodObj)
    External (\_SB.PCI0.GFX0.DD02, DeviceObj)

    Scope (\_GPE)
    {
        // Firmware _Q86/_Q87 and HP SHKF call G001 with ACPI video events.
        // BrightnessKeys has a DD02 fallback; explicitly deliver these events there.
        // Other events and other operating systems retain the firmware implementation.
        Method (G001, 1, Serialized)
        {
            If (_OSI ("Darwin"))
            {
                If (LOr (LEqual (Arg0, 0x86), LEqual (Arg0, 0x87)))
                {
                    Notify (\_SB.PCI0.GFX0.DD02, Arg0)
                    Return (Zero)
                }
            }
            Z001 (Arg0)
            Return (Zero)
        }
    }
}
