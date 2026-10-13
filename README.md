# Computer Networks - 15 Record Exercises

Exactly 15 numbered record entries. Each Exercise_NN folder contains its own full record PDF, relevant complete program/configuration, diagrams and clearly labelled actual/expected outputs.

All original manual exercises are preserved. Echo and chat (TCP/UDP) are parts of Exercise 12, rather than extra numbered exercises.

| Exercise | Title | Record PDF | Files |
| --- | --- | --- | --- |
| 01 | Study of various Network commands used in Linux and Windows | [Open PDF](Exercise_01/CN_Exercise_01.pdf) | [Exercise files](Exercise_01/README.md) |
| 02 | Study of Network cables | [Open PDF](Exercise_02/CN_Exercise_02.pdf) | [Exercise files](Exercise_02/README.md) |
| 03 | Experiments on CISCO PACKET TRACER (Simulation Tool) | [Open PDF](Exercise_03/CN_Exercise_03.pdf) | [Exercise files](Exercise_03/README.md) |
| 04 | Setup and configure a LAN (Local area network) using a Switch and Ethernet cables in your lab | [Open PDF](Exercise_04/CN_Exercise_04.pdf) | [Exercise files](Exercise_04/README.md) |
| 05 | Experiments on Packet capture tool: Wireshark | [Open PDF](Exercise_05/CN_Exercise_05.pdf) | [Exercise files](Exercise_05/README.md) |
| 06 | Error Correction at Data Link Layer | [Open PDF](Exercise_06/CN_Exercise_06.pdf) | [Exercise files](Exercise_06/README.md) |
| 07 | Flow control at Data Link Layer | [Open PDF](Exercise_07/CN_Exercise_07.pdf) | [Exercise files](Exercise_07/README.md) |
| 08 | NMAP to Discover Live Hosts Using Nmap Scans (ARP, ICMP, TCP/UDP) on the TryHackMe Platform | [Open PDF](Exercise_08/CN_Exercise_08.pdf) | [Exercise files](Exercise_08/README.md) |
| 09 | Implementation of SUBNETTING in CISCO PACKET TRACER simulator | [Open PDF](Exercise_09/CN_Exercise_09.pdf) | [Exercise files](Exercise_09/README.md) |
| 10 | Internetworking with routers in CISCO PACKET TRACER simulator | [Open PDF](Exercise_10/CN_Exercise_10.pdf) | [Exercise files](Exercise_10/README.md) |
| 11 | Routing at Network Layer | [Open PDF](Exercise_11/CN_Exercise_11.pdf) | [Exercise files](Exercise_11/README.md) |
| 12 | End-End Communication at Transport Layer | [Open PDF](Exercise_12/CN_Exercise_12.pdf) | [Exercise files](Exercise_12/README.md) |
| 13 | Implement your own ping program | [Open PDF](Exercise_13/CN_Exercise_13.pdf) | [Exercise files](Exercise_13/README.md) |
| 14 | Write a code using RAW sockets to implement packet sniffing | [Open PDF](Exercise_14/CN_Exercise_14.pdf) | [Exercise files](Exercise_14/README.md) |
| 15 | Analyse various types of servers using Webalizer tool | [Open PDF](Exercise_15/CN_Exercise_15.pdf) | [Exercise files](Exercise_15/README.md) |

## Using the files

Open each numbered PDF for the record. Run commands from this package root unless a cd command is shown. The experiment source/configuration files are in the matching folder.

Programming exercises provide full Python implementations. Tool and hardware exercises provide the required commands/configurations. Actual execution and expected outcomes remain distinct; physical/tool runs not performed are not claimed.

This package is separate from the handwritten 30-page observation record. Published as the College account project techky-Kabilan/Computer-Networks-Lab.


## Verified programs and evidence

The complete Python programs are in Exercise_06 (Hamming), Exercise_07 (sliding window), Exercise_12 (TCP/UDP echo and chat), Exercise_13 (custom ICMP ping), and Exercise_14 (raw capture/decoder). Other exercises provide their required configurations and commands.

13 portable tests passed, including 3,072 Hamming single-bit correction cases and real localhost TCP/UDP communication. The project also includes actual raw ICMP localhost replies and a real 100-packet Wireshark loopback capture. Linux raw capture, physical equipment, Packet Tracer, TryHackMe and Webalizer operational results remain explicitly labelled pending/expected.

[Verification evidence](verification/README.md)

```text
python -m unittest discover -s tests -v
python -m pip install -r requirements.txt
python tools/build_record_pdfs.py
python tools/check_record.py
```
