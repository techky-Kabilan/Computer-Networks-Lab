# Exercise 02: Learning and Assignment of IP Address manually to computers

[Open the PDF](CN_Exercise_02.pdf)

## Aim

To learn IPv4 addressing and manually assign unique static addresses to two lab computers.

## Requirements

Two lab computers, switch, Ethernet cables; Windows IPv4 settings or Linux NetworkManager.

## Procedure / algorithm

1. Identify the assigned Ethernet interface and record the current DHCP configuration.
2. Connect both PCs to the switch; use the addressing table and check that the chosen addresses are unused.
3. Set the IPv4 address, /24 mask and gateway on each PC. Configure DNS only when the specified service exists.
4. Verify the address and connected route; ping the peer and gateway. Check the firewall ICMP setting if replies are blocked.
5. Compare the network portion 192.168.20 with the distinct host portions 11 and 12; restore the original configuration after the lab.

## Complete code / configuration

### [addressing.csv](addressing.csv)

```
device,IPv4,mask,gateway,DNS
PC1,192.168.20.11,255.255.255.0,192.168.20.1,192.168.20.1
PC2,192.168.20.12,255.255.255.0,192.168.20.1,192.168.20.1
Router,192.168.20.1,255.255.255.0,none,none

```

### [configuration.txt](configuration.txt)

```
Windows graphical configuration:
Settings > Network & Internet > Advanced network settings > More network adapter options.
Open the lab Ethernet adapter Properties > Internet Protocol Version 4 (TCP/IPv4).
Select Use the following IP address; enter the assigned row in addressing.csv.
Enter DNS only if 192.168.20.1 provides the lab DNS service.
Verify: ipconfig /all
Verify PC1 to PC2: ping 192.168.20.12
Verify gateway: ping 192.168.20.1
Restore Obtain an IP address automatically / DNS automatically after the lab.

Linux NetworkManager (replace LAB-ETH with the lab connection name):
nmcli connection show
sudo nmcli connection modify 'LAB-ETH' ipv4.method manual ipv4.addresses 192.168.20.11/24 ipv4.gateway 192.168.20.1 ipv4.dns 192.168.20.1
sudo nmcli connection up 'LAB-ETH'
ip -4 address show
ip route show
ping -c 4 192.168.20.12
Restore: sudo nmcli connection modify 'LAB-ETH' ipv4.method auto ipv4.addresses '' ipv4.gateway '' ipv4.dns ''
sudo nmcli connection up 'LAB-ETH'

```

## Actual output

Not executed in the required lab/tool environment.

## Expected output

Both PCs show their assigned addresses and can exchange ICMP replies; a configured, connected gateway replies.

## Observations

A /24 mask places both addresses in the same subnet. A gateway is needed for off-subnet traffic; DNS resolves names, not numeric addresses.

## Result

The static-address plan and complete configuration steps are supplied. Live interface settings were not changed here.
