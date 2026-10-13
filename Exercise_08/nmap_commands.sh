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
