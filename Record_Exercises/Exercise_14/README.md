# Exercise 14: To capture, save, and analyze network traffic on TCP / UDP / IP / HTTP / ARP /DHCP /ICMP /DNS using Wireshark Tool

**Exercise 14** · [Download this exercise PDF](https://github.com/techky-Kabilan/Computer-Networks-Lab/raw/refs/heads/main/Record_Exercises/Exercise_14/CN_Exercise_14.pdf)

Read the complete exercise below. The download opens the PDF file directly.

## Aim

To understand Wireshark packet capture and encapsulation at the layers of a protocol stack.

## Requirements

Wireshark/TShark, capture support, active lab interface and traffic generators.

## Procedure / algorithm

1. Choose the active Ethernet interface and configure capture stopping after 100 packets. Save the captured packets.
2. Inspect Packet List, Packet Details and Packet Bytes. Expand link, IP and transport/application headers.
3. Apply the supplied TCP/UDP, ARP, DNS, HTTP, IP/ICMP and DHCP display filters. Record the addresses and fields actually present.
4. Generate lab DNS/web/ping/DHCP traffic as needed. For TCP/UDP and DNS, inspect Statistics > Flow Graph; for TCP, use Follow > TCP Stream.
5. Distinguish capture filters, which select stored traffic, from display filters, which select visible saved traffic.
6. For this submission, capture only project-generated localhost TCP/UDP echo and localhost ICMP. Analyse the resulting 100-packet file with TShark.

## Complete code / configuration

### [capture_commands.txt](capture_commands.txt)

```
GUI: Capture > Options > active Ethernet interface > stop after 100 packets.
Generate assigned lab traffic, save capture.pcapng, then use display_filters.txt.
Statistics > Flow Graph; Follow > TCP Stream.
CLI for assigned Ethernet interface:
tshark -D
tshark -i INTERFACE_NUMBER -c 100 -w capture.pcapng
tshark -r capture.pcapng -Y "tcp or udp"
tshark -r capture.pcapng -Y arp
tshark -r capture.pcapng -Y dns
tshark -r capture.pcapng -Y http
tshark -r capture.pcapng -Y "ip or icmp"
tshark -r capture.pcapng -Y "udp.port == 67 or udp.port == 68"
tshark -r capture.pcapng -q -z io,phs

```

### [display_filters.txt](display_filters.txt)

```
tcp or udp
arp
dns
http
ip or icmp
udp.port == 67 or udp.port == 68
ip.addr == 127.0.0.1
tcp.port == 50990
udp.port == 50991

```

## Actual output

```
ACTUAL TSHARK ANALYSIS OF 100 LIVE LOOPBACK PACKETS
Own TCP/UDP echo traffic and ICMP to 127.0.0.1 only.
This is loopback, not the manual's physical Ethernet capture.
ARP, DNS, HTTP and DHCP lab captures remain pending.

Frame	Source	Destination	Protocol
1	127.0.0.1	127.0.0.1	ICMP
2	127.0.0.1	127.0.0.1	ICMP
3	127.0.0.1	127.0.0.1	ICMP
4	127.0.0.1	127.0.0.1	ICMP
5	127.0.0.1	127.0.0.1	UDP
6	127.0.0.1	127.0.0.1	UDP
7	127.0.0.1	127.0.0.1	UDP
8	127.0.0.1	127.0.0.1	UDP
9	127.0.0.1	127.0.0.1	UDP
10	127.0.0.1	127.0.0.1	UDP
11	127.0.0.1	127.0.0.1	UDP
12	127.0.0.1	127.0.0.1	UDP
13	127.0.0.1	127.0.0.1	UDP
14	127.0.0.1	127.0.0.1	UDP
15	127.0.0.1	127.0.0.1	UDP
16	127.0.0.1	127.0.0.1	UDP
17	127.0.0.1	127.0.0.1	UDP
18	127.0.0.1	127.0.0.1	UDP
19	127.0.0.1	127.0.0.1	UDP
20	127.0.0.1	127.0.0.1	UDP
21	127.0.0.1	127.0.0.1	UDP
22	127.0.0.1	127.0.0.1	UDP
23	127.0.0.1	127.0.0.1	UDP
24	127.0.0.1	127.0.0.1	UDP
25	127.0.0.1	127.0.0.1	UDP
26	127.0.0.1	127.0.0.1	UDP
27	127.0.0.1	127.0.0.1	TCP
28	127.0.0.1	127.0.0.1	TCP
29	127.0.0.1	127.0.0.1	TCP
30	127.0.0.1	127.0.0.1	TCP
31	127.0.0.1	127.0.0.1	TCP
32	127.0.0.1	127.0.0.1	TCP
33	127.0.0.1	127.0.0.1	TCP
34	127.0.0.1	127.0.0.1	TCP
35	127.0.0.1	127.0.0.1	TCP
36	127.0.0.1	127.0.0.1	TCP
37	127.0.0.1	127.0.0.1	TCP
38	127.0.0.1	127.0.0.1	TCP
39	127.0.0.1	127.0.0.1	TCP
40	127.0.0.1	127.0.0.1	TCP
41	127.0.0.1	127.0.0.1	TCP
42	127.0.0.1	127.0.0.1	TCP
43	127.0.0.1	127.0.0.1	TCP
44	127.0.0.1	127.0.0.1	TCP
45	127.0.0.1	127.0.0.1	TCP
46	127.0.0.1	127.0.0.1	TCP
47	127.0.0.1	127.0.0.1	TCP
48	127.0.0.1	127.0.0.1	TCP
49	127.0.0.1	127.0.0.1	TCP
50	127.0.0.1	127.0.0.1	TCP
51	127.0.0.1	127.0.0.1	TCP
52	127.0.0.1	127.0.0.1	TCP
53	127.0.0.1	127.0.0.1	TCP
54	127.0.0.1	127.0.0.1	TCP
55	127.0.0.1	127.0.0.1	TCP
56	127.0.0.1	127.0.0.1	TCP
57	127.0.0.1	127.0.0.1	TCP
58	127.0.0.1	127.0.0.1	TCP
59	127.0.0.1	127.0.0.1	TCP
60	127.0.0.1	127.0.0.1	TCP
61	127.0.0.1	127.0.0.1	TCP
62	127.0.0.1	127.0.0.1	TCP
63	127.0.0.1	127.0.0.1	TCP
64	127.0.0.1	127.0.0.1	TCP
65	127.0.0.1	127.0.0.1	TCP
66	127.0.0.1	127.0.0.1	TCP
67	127.0.0.1	127.0.0.1	TCP
68	127.0.0.1	127.0.0.1	TCP
69	127.0.0.1	127.0.0.1	TCP
70	127.0.0.1	127.0.0.1	TCP
71	127.0.0.1	127.0.0.1	TCP
72	127.0.0.1	127.0.0.1	TCP
73	127.0.0.1	127.0.0.1	TCP
74	127.0.0.1	127.0.0.1	TCP
75	127.0.0.1	127.0.0.1	TCP
76	127.0.0.1	127.0.0.1	TCP
77	127.0.0.1	127.0.0.1	TCP
78	127.0.0.1	127.0.0.1	TCP
79	127.0.0.1	127.0.0.1	TCP
80	127.0.0.1	127.0.0.1	TCP
81	127.0.0.1	127.0.0.1	TCP
82	127.0.0.1	127.0.0.1	TCP
83	127.0.0.1	127.0.0.1	TCP
84	127.0.0.1	127.0.0.1	TCP
85	127.0.0.1	127.0.0.1	TCP
86	127.0.0.1	127.0.0.1	TCP
87	127.0.0.1	127.0.0.1	TCP
88	127.0.0.1	127.0.0.1	TCP
89	127.0.0.1	127.0.0.1	TCP
90	127.0.0.1	127.0.0.1	TCP
91	127.0.0.1	127.0.0.1	TCP
92	127.0.0.1	127.0.0.1	TCP
93	127.0.0.1	127.0.0.1	TCP
94	127.0.0.1	127.0.0.1	TCP
95	127.0.0.1	127.0.0.1	TCP
96	127.0.0.1	127.0.0.1	TCP
97	127.0.0.1	127.0.0.1	TCP
98	127.0.0.1	127.0.0.1	TCP
99	127.0.0.1	127.0.0.1	TCP
100	127.0.0.1	127.0.0.1	TCP

```

## Expected output

TCP shows SYN/SYN-ACK/ACK and data; ARP shows address resolution; DNS query/response; ICMP Echo Request/Reply; DHCP Discover/Offer/Request/ACK. HTTPS does not expose ordinary unencrypted HTTP fields.

## Observations

Actual evidence is a 100-packet Npcap loopback capture, not physical IEEE 802.3 Ethernet. It contains ICMP, UDP and TCP. ARP/DNS/HTTP/DHCP captures and GUI screenshots are pending. ARP has no transport header; DNS commonly uses UDP 53 (also TCP); HTTP uses TCP 80. Promiscuous mode sees only traffic delivered to the interface.

## Result

A real 100-packet local capture was saved and analysed; remaining manual Ethernet/protocol exercises are documented but not claimed as executed.
