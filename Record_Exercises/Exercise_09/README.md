# Exercise 09: Design a simple topology and configure with one router, two switches and PCs using Cisco Packet Tracer

[Open the PDF](CN_Exercise_09.pdf)

## Aim

To construct two switched LANs interconnected by one router and verify communication in Packet Tracer.

## Requirements

Packet Tracer; one 2911 router, two 2960 switches and four PCs.

## Procedure / algorithm

1. Place devices and cable them using topology.txt.
2. Assign each PC its unique IPv4 address, mask and router-interface gateway from addressing.csv.
3. Apply R1.cfg and switch.cfg; ensure both routed interfaces are administratively enabled.
4. Wait for links to turn green; verify connected routes and MAC learning.
5. Ping within each LAN and across LANs; inspect ARP/ICMP in Simulation mode.

## Complete code / configuration

### [addressing.csv](addressing.csv)

```
device,interface,IPv4,mask,gateway
R1,GigabitEthernet0/0,192.168.10.1,255.255.255.0,none
R1,GigabitEthernet0/1,192.168.20.1,255.255.255.0,none
PC1,FastEthernet0,192.168.10.11,255.255.255.0,192.168.10.1
PC2,FastEthernet0,192.168.10.12,255.255.255.0,192.168.10.1
PC3,FastEthernet0,192.168.20.11,255.255.255.0,192.168.20.1
PC4,FastEthernet0,192.168.20.12,255.255.255.0,192.168.20.1

```

### [R1.cfg](R1.cfg)

```
enable
configure terminal
hostname R1
interface GigabitEthernet0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 192.168.20.1 255.255.255.0
 no shutdown
end
copy running-config startup-config
show ip interface brief
show ip route

```

### [switch.cfg](switch.cfg)

```
enable
configure terminal
interface range FastEthernet0/1-3
 switchport mode access
 no shutdown
end
copy running-config startup-config
show mac address-table

```

### [topology.txt](topology.txt)

```
PC1 --- Fa0/1 SW1 Fa0/3 --- Gi0/0 R1 Gi0/1 --- Fa0/3 SW2 Fa0/1 --- PC3
PC2 --- Fa0/2 SW1                                 SW2 Fa0/2 --- PC4
All links use copper straight-through Ethernet cables.
R1: 2911; SW1/SW2: 2960. Apply switch.cfg to both switches.
PC1: ping 192.168.10.12
PC1: ping 192.168.20.11
PC4: ping 192.168.10.11

```

## Actual output

Not executed in the required lab/tool environment.

## Expected output

Both connected networks appear in the routing table; after ARP resolution all PCs can communicate.

## Observations

No static routes are needed because both subnets are directly connected to R1. Hosts need their local router address as the gateway.

## Result

The complete topology and device configuration are prepared. Packet Tracer execution remains pending.
