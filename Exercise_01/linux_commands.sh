#!/usr/bin/env bash
set -euo pipefail
hostname
ip address show
ip link show
ip route show
ip neigh show
ping -c 4 127.0.0.1
# Optional installed tools and assigned lab targets:
# ifconfig; netstat -an; mtr -n -c 10 TARGET_IP
# nslookup TARGET_DOMAIN; sudo tcpdump -i eth0 -c 10
