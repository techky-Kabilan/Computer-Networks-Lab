# Exercise 12: Nmap to discover live hosts using ARP scan, ICMP scan, and TCP/UDP ping scan in TryHackMe Platform.

[Open the PDF](CN_Exercise_12.pdf)

## Aim

To discover live hosts using ARP, ICMP and TCP/UDP discovery probes on an assigned TryHackMe lab network.

## Requirements

TryHackMe Nmap Live Host Discovery room, AttackBox/VPN and an assigned target; Nmap.

## Procedure / algorithm

1. Start the TryHackMe lab machine and AttackBox or approved VPN machine. Identify the assigned target/subnet.
2. Preview targets using -sL -n; supply a host, range, CIDR block or -iL list. For 10.10.12.13/29 the block contains addresses .8-.15.
3. Run ARP discovery (-PR -sn) for local Ethernet hosts. Compare ICMP Echo (-PE), Timestamp (-PP) and Mask (-PM) discovery.
4. Run TCP SYN (-PS), TCP ACK (-PA) and UDP (-PU) discovery. Use --disable-arp-ping to compare IP probes on a local link.
5. Observe SYN/ACK or RST for SYN probes; RST for ACK probes; UDP response or ICMP port unreachable for UDP probes. No response is inconclusive.

## Complete code / configuration

### [nmap_commands.sh](nmap_commands.sh)

```
#!/usr/bin/env bash
set -euo pipefail
TARGETS="${1:?Supply the assigned TryHackMe target or subnet}"
nmap -sL -n "$TARGETS"
sudo nmap -sn -PR "$TARGETS"
sudo nmap -sn -PE --disable-arp-ping "$TARGETS"
sudo nmap -sn -PP --disable-arp-ping "$TARGETS"
sudo nmap -sn -PM --disable-arp-ping "$TARGETS"
sudo nmap -sn -PS80,443 --disable-arp-ping "$TARGETS"
sudo nmap -sn -PA80 --disable-arp-ping "$TARGETS"
sudo nmap -sn -PU40125 --disable-arp-ping "$TARGETS"
# Other target forms: -iL list_of_hosts.txt, an IP range, or CIDR subnet.
# -n skips DNS; -R requests all reverse lookups; --dns-servers selects DNS.

```

## Actual output

Not executed in the required lab/tool environment.

## Expected output

Hosts responding to the permitted discovery probes are listed as up with reasons where available. Results depend on the assigned lab hosts and firewall rules.

## Observations

ARP discovery works on local-link IPv4 hosts. Firewalls may suppress probes, so lack of a response is inconclusive. -sn disables port scanning; -Pn skips discovery; DNS resolution can be suppressed using -n.

## Result

Complete host-discovery commands and observations are supplied; no TryHackMe/Nmap live scan was executed here.
