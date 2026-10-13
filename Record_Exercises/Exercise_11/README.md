# Exercise 11: Examine Network Address Translation (NAT) using Cisco Packet Tracer

**Exercise 11** · [Download this exercise PDF](https://github.com/techky-Kabilan/Computer-Networks-Lab/raw/refs/heads/main/Record_Exercises/Exercise_11/CN_Exercise_11.pdf)

Read the complete exercise below. The download opens the PDF file directly.

## Aim

To configure and examine NAT overload (PAT) in Packet Tracer.

## Requirements

Packet Tracer; two routers, switch, two inside PCs and an outside HTTP server.

## Procedure / algorithm

1. Build the labelled inside/outside topology and assign addressing.csv.
2. Configure R1 inside/outside interfaces, the inside-source access list, overload and default route.
3. Apply ISP.cfg and enable HTTP on the outside server.
4. Generate ping and HTTP traffic from both inside PCs, then immediately inspect NAT translations/statistics.
5. Compare inside-local/private addresses with the shared inside-global address and distinct ports/identifiers.

## Complete code / configuration

### [addressing.csv](addressing.csv)

```
device,interface,IPv4,mask,gateway
PC1,FastEthernet0,192.168.40.11,255.255.255.0,192.168.40.1
PC2,FastEthernet0,192.168.40.12,255.255.255.0,192.168.40.1
R1,GigabitEthernet0/0,192.168.40.1,255.255.255.0,none
R1,GigabitEthernet0/1,203.0.113.2,255.255.255.252,none
ISP,GigabitEthernet0/0,203.0.113.1,255.255.255.252,none
ISP,GigabitEthernet0/1,198.51.100.1,255.255.255.0,none
Server,FastEthernet0,198.51.100.10,255.255.255.0,198.51.100.1

```

### [R1.cfg](R1.cfg)

```
enable
configure terminal
hostname R1
interface GigabitEthernet0/0
 ip address 192.168.40.1 255.255.255.0
 ip nat inside
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 203.0.113.2 255.255.255.252
 ip nat outside
 no shutdown
exit
access-list 1 permit 192.168.40.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload
ip route 0.0.0.0 0.0.0.0 203.0.113.1
end
copy running-config startup-config
show ip nat translations
show ip nat statistics
show ip route

```

### [ISP.cfg](ISP.cfg)

```
enable
configure terminal
hostname ISP
interface GigabitEthernet0/0
 ip address 203.0.113.1 255.255.255.252
 no shutdown
exit
interface GigabitEthernet0/1
 ip address 198.51.100.1 255.255.255.0
 no shutdown
end
copy running-config startup-config

```

### [topology.txt](topology.txt)

```
PC1 --       SW1 -- R1 Gi0/0 [inside] Gi0/1 -- ISP Gi0/0 Gi0/1 -- Server
PC2 --/
R1/ISP: 2911 routers; SW1: 2960; Server: Server-PT.
Use addressing.csv and copper straight-through cables for host/switch links.
Use automatic cable choice for direct router/router and router/server links.
Enable HTTP under Server > Services > HTTP.
PC1 and PC2: ping 198.51.100.10
PC1 web browser: http://198.51.100.10
R1 immediately after traffic: show ip nat translations
Inside local: 192.168.40.11 / 192.168.40.12
Inside global: 203.0.113.2 (shared using distinct ports/ICMP identifiers)
Outside global: 198.51.100.10
ISP deliberately has no route to 192.168.40.0/24; return traffic uses NAT.

```

## Actual output

Not executed in the required lab/tool environment.

## Expected output

Inside hosts receive replies and open the HTTP page; the translation table shows both private hosts translated to 203.0.113.2.

## Observations

PAT shares an interface address through transport ports or ICMP identifiers. Translation entries may expire, so observe them while generating traffic.

## Result

Complete NAT/PAT configuration and verification commands are supplied. Packet Tracer execution is pending.
