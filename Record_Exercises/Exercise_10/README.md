# Exercise 10: Customize Switch with Network Modules using Cisco Packet Tracer

[Open the PDF](CN_Exercise_10.pdf)

## Aim

To customize a modular switch with supported network modules and verify the added ports.

## Requirements

Packet Tracer; Switch-PT-Empty, supported copper/fibre modules, two PCs and matching cables.

## Procedure / algorithm

1. Inspect the empty modular chassis in Physical view and its available compatible modules.
2. Power off, add the copper modules to vacant slots, and power on.
3. Identify the new interface names; configure active access ports and connect the two PCs.
4. Assign the same-subnet host addresses in switch_commands.txt and verify ping/MAC learning.
5. Optionally add matching fibre modules to two powered-off switches and test a fibre uplink; record the actual module types and port count.

## Complete code / configuration

### [modules.txt](modules.txt)

```
Device: Switch-PT-Empty (modular switch), not a fixed-port 2960.
1. Place Switch-PT-Empty; open Physical view.
2. Switch the device off before inserting/removing modules.
3. Insert supported PT-SWITCH-NM-1CFE copper Fast Ethernet modules
   into three available slots shown by the installed Packet Tracer version.
4. Power on; open Config/CLI and identify the actual interface names.
5. Attach two PC-PT hosts to two copper Fast Ethernet ports.
6. For a fibre demonstration, power off and add a supported fibre module
   to each of two Switch-PT devices, then use the matching fibre cable.
7. Power on, inspect link state and verify the module/port inventory.
Module availability and resulting slot/interface numbering are version-specific.
Do not paste fixed interface names until show interfaces identifies them.

```

### [switch_commands.txt](switch_commands.txt)

```
enable
show interfaces
show ip interface brief
configure terminal
hostname ModularSwitch
! Use the actual first populated copper port, e.g. FastEthernet0/1:
interface FastEthernet0/1
 switchport mode access
 no shutdown
exit
! Use the actual second populated copper port, e.g. FastEthernet1/1:
interface FastEthernet1/1
 switchport mode access
 no shutdown
end
copy running-config startup-config
show mac address-table
PC1: IPv4 192.168.30.11, mask 255.255.255.0, gateway blank
PC2: IPv4 192.168.30.12, mask 255.255.255.0, gateway blank
PC1 command prompt: ping 192.168.30.12

```

## Actual output

Not executed in the required lab/tool environment.

## Expected output

The new interfaces appear after power-on and connected copper/fibre ports show working links. Same-subnet PCs exchange replies.

## Observations

Fixed-port switches cannot be treated as empty modular chassis. Module type, cable and peer interface must match; numbering depends on the chosen slots/version.

## Result

The module installation, configuration and observation steps are prepared. Packet Tracer module changes have not been performed here.
