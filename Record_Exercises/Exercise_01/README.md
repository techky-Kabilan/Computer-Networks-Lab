# Exercise 01: Basic Networking Commands in Linux and Windows operating systems

[Open the PDF](CN_Exercise_01.pdf)

## Aim

To study and practise network commands used in Linux and Windows.

## Requirements

Windows Command Prompt or PowerShell; a Linux terminal; an assigned lab host/domain for remote tests.

## Procedure / algorithm

1. Run hostname, ipconfig /all (Windows) or ip address show (Linux). Note IP, mask, gateway and DNS for the active interface.
2. Test loopback, a same-subnet host and the gateway using ping. Use tracert/pathping on Windows or mtr on Linux to examine hops and loss.
3. Inspect neighbour mappings with arp -a or ip neigh show; inspect connection/port status with netstat -an and routing with route print or ip route show.
4. Query DNS using nslookup. Use nbtstat for NetBIOS name information when relevant.
5. On the assigned Linux lab interface, use the configuration commands to change IPv4/IPv6 settings and activate the NetworkManager profile. Verify address, route and DNS again.
6. Capture ten assigned-interface packets with tcpdump. Diagnose failures by checking cable, link state, addresses, routes and name resolution.

## Complete code / configuration

### [configuration_commands.txt](configuration_commands.txt)

```
LINUX - apply only to the interface/profile assigned in the lab:
sudo ip address add 192.168.1.10/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 192.168.1.254 dev eth0
ip route get 10.10.1.4
sudo tcpdump -i eth0 -c 10 host 8.8.8.8
sudo tcpdump -i eth0 port 53
nmcli connection show
sudo nmcli connection modify "Wired connection 1" ipv4.method manual ipv4.addresses 192.0.2.1/24 ipv4.gateway 192.0.2.254 ipv4.dns 192.0.2.200 ipv4.dns-search example.com
sudo nmcli connection modify "Wired connection 1" ipv6.method manual ipv6.addresses 2001:db8:1::fffe/64 ipv6.gateway 2001:db8:1::ffee ipv6.dns 2001:db8:1::ffbb
sudo nmcli connection up "Wired connection 1"
ip address show
ip -6 route show default
cat /etc/resolv.conf
To restore automatic addressing:
sudo nmcli connection modify "Wired connection 1" ipv4.method auto ipv4.addresses "" ipv4.gateway "" ipv4.dns ""
sudo nmcli connection modify "Wired connection 1" ipv6.method auto ipv6.addresses "" ipv6.gateway "" ipv6.dns ""
sudo nmcli connection up "Wired connection 1"

```

### [linux_commands.sh](linux_commands.sh)

```
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

```

### [windows_commands.ps1](windows_commands.ps1)

```
# Read-only networking commands; no host settings are changed.
hostname
ipconfig /all
arp -a
netstat -an
netstat -r
route print
ping -n 4 127.0.0.1
# For the assigned lab host/domain, also use:
# tracert TARGET_IP
# pathping TARGET_IP
# nslookup TARGET_DOMAIN
# nbtstat -a TARGET_HOSTNAME

```

## Actual output

```
ACTUAL WINDOWS COMMAND: ping -n 2 127.0.0.1

Pinging 127.0.0.1 with 32 bytes of data:
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128

Ping statistics for 127.0.0.1:
    Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

```

## Expected output

Assigned hosts reply to ping; route commands show connected/default routes; DNS queries return the configured answer. Output addresses, ports and hop counts depend on the lab network.

## Observations

Echo Replies indicate ICMP reachability; timeout indicates no reply, and DNS errors indicate name-resolution failure. The actual record is a Windows loopback ping only. Linux configuration and remote-target commands were not applied to this computer.

## Result

Windows loopback connectivity was verified. Complete Linux/Windows command and configuration references are supplied; remaining commands require the assigned lab environment.
