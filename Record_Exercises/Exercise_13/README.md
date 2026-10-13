# Exercise 13: Demonstrate network forensics using PcapXray tool

[Open the PDF](CN_Exercise_13.pdf)

## Aim

To perform offline network forensics on a packet capture using PcapXray.

## Requirements

Linux lab workstation; PcapXray, Tkinter, Graphviz and supplied synthetic PCAP.

## Procedure / algorithm

1. Set up the upstream tool using pcapxray_commands.txt and open the GUI.
2. Select sample.pcap, an output directory and the auto parser; start Analyze.
3. Generate the network diagram using Visualize and inspect the endpoint/protocol/session details.
4. Record source/destination addresses, ports, communication directions and packet counts.
5. Cross-check the supplied capture with TShark. Treat heuristic warnings as leads requiring packet-level evidence.

## Complete code / configuration

### [pcapxray_commands.txt](pcapxray_commands.txt)

```
Linux lab setup (current upstream PcapXray):
sudo apt-get update
sudo apt-get install -y python3-tk graphviz tshark git
git clone https://github.com/srixivas/PcapXray.git
cd PcapXray
python3 -m venv .venv --system-site-packages
source .venv/bin/activate
python -m pip install -r requirements.txt
python Source/main.py

Offline file analysis:
Choose supplied sample.pcap under the record exercise folder.
Choose an output directory and the auto engine.
Click Analyze!, then Visualize!.
Inspect devices, protocol classifications and communication flows.
Save the report/network diagram and document the observed endpoints.
No root privilege is required for offline file analysis.

Independent fixture cross-check (not PcapXray output):
tshark -r sample.pcap -T fields -e frame.number -e ip.src -e ip.dst -e udp.srcport -e udp.dstport

```

[Download the synthetic capture](sample.pcap)

## Actual output

```
Actual independent fixture verification; NOT PcapXray output.
{
  "destination_ip": "192.0.2.20",
  "destination_mac": "00:11:22:33:44:55",
  "destination_port": 9999,
  "ethertype": "0x0800",
  "header_length": 20,
  "length": 47,
  "protocol": "UDP",
  "source_ip": "192.0.2.10",
  "source_mac": "66:77:88:99:aa:bb",
  "source_port": 12345,
  "ttl": 64,
  "udp_length": 27
}
PCAP: 1 Ethernet/IPv4/UDP packet; no live traffic.

```

## Expected output

The supplied synthetic fixture contains one UDP packet from 192.0.2.10:12345 to 192.0.2.20:9999. The diagram should show these endpoints and their communication.

## Observations

The independent PCAP fixture check is actual; it is not a claimed PcapXray GUI run. Synthetic endpoints do not establish device identity or malicious activity.

## Result

The PCAP, setup commands and forensic procedure are prepared; fixture content was checked, but PcapXray GUI analysis remains pending.
