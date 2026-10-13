# CS23532 Computer Networks â€” Document-Matched Record Exercises

This set follows the exact 15 titles in Computer Networks Record.docx. It is separate from the previously published manual-based exercises and the handwritten observation record. Each folder includes a complete PDF, source/configuration, procedure, output and result. Actual checks and expected lab outcomes are explicitly separated.

| Exercise | Original record title | Record |
|---|---|---|
| 1 | Basic Networking Commands in Linux and Windows operating systems | [PDF](Exercise_01/CN_Exercise_01.pdf) |
| 2 | Learning and Assignment of IP Address manually to computers | [PDF](Exercise_02/CN_Exercise_02.pdf) |
| 3 | Study of different types of Network Cables and Crimping of cable with RJ45 connector | [PDF](Exercise_03/CN_Exercise_03.pdf) |
| 4 | Implement packet sniffing using raw sockets in python | [PDF](Exercise_04/CN_Exercise_04.pdf) |
| 5 | Develop a customized ping command to test the server connectivity | [PDF](Exercise_05/CN_Exercise_05.pdf) |
| 6 | Building anonymous FTP Scanner using ftplib module | [PDF](Exercise_06/CN_Exercise_06.pdf) |
| 7 | Develop a simple calculator using XMLRPC | [PDF](Exercise_07/CN_Exercise_07.pdf) |
| 8 | Develop a program to create reverse shell using TCP sockets | [PDF](Exercise_08/CN_Exercise_08.pdf) |
| 9 | Design a simple topology and configure with one router, two switches and PCs using Cisco Packet Tracer | [PDF](Exercise_09/CN_Exercise_09.pdf) |
| 10 | Customize Switch with Network Modules using Cisco Packet Tracer | [PDF](Exercise_10/CN_Exercise_10.pdf) |
| 11 | Examine Network Address Translation (NAT) using Cisco Packet Tracer | [PDF](Exercise_11/CN_Exercise_11.pdf) |
| 12 | Nmap to discover live hosts using ARP scan, ICMP scan, and TCP/UDP ping scan in TryHackMe Platform. | [PDF](Exercise_12/CN_Exercise_12.pdf) |
| 13 | Demonstrate network forensics using PcapXray tool | [PDF](Exercise_13/CN_Exercise_13.pdf) |
| 14 | To capture, save, and analyze network traffic on TCP / UDP / IP / HTTP / ARP /DHCP /ICMP /DNS using Wireshark Tool | [PDF](Exercise_14/CN_Exercise_14.pdf) |
| 15 | To Analyze the different types of servers using Webalizer tool | [PDF](Exercise_15/CN_Exercise_15.pdf) |

## Verification

See [checks](verification/checks.txt). Program tests use localhost and synthetic fixtures. Packet Tracer configurations, physical labs, TryHackMe, PcapXray GUI and Webalizer require their lab environments.

## References

- [Python ftplib](https://docs.python.org/3/library/ftplib.html)
- [Python XML-RPC server](https://docs.python.org/3/library/xmlrpc.server.html)
- [Cisco NAT configuration](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html)
- [PcapXray setup and usage](https://github.com/srixivas/PcapXray)

No student details, dates or signatures are included in this project.

## Reproduce program checks / PDFs

```
python -m pip install -r requirements.txt
python tools/verify_programs.py
python tools/build_record_pdfs.py
```
