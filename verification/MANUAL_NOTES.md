# Manual provenance and interpretation

Source: uploaded **CS23532_CN_Labmanual_2025-26 (1).pdf**, 100 pages. The downloaded copy was confirmed byte-identical to the uploaded attachment during the earlier observation-record work. Source files under the synced project directory were left unchanged, and the original manual is not redistributed.

| Experiment | Manual PDF pages | Interpretation |
| --- | --- | --- |
| 01 | 6-13 | Command reference; live evidence limited to localhost ping. Linux address changes not applied to this computer. |
| 02 | 14-19 | Pin standards retained. Correct cable capabilities replace blanket fibre-distance and category-speed errors. |
| 03 | 20-23 | Hub, switch and mixed topologies; no invented campus topology. |
| 04 | 24-26 | Manual's 10.1.1.x/8 addresses; switch management uses an SVI. |
| 05 | 27-39 | All filters/procedures included. Actual capture is explicitly loopback, not the manual's physical Ethernet test. |
| 06 | 40 | Complete bytewise Hamming implementation authored for the stated text/channel requirements. |
| 07 | 41 | File-buffer sliding window with manual and automatic fault injection; optional piggybacking is not claimed. |
| 08 | 42-59 | Nmap discovery plus wireless Part B remain one experiment. WEP is labelled a legacy simulation setting. |
| 09 | 60-63 | /24-to-/27 maths separated from the four different LAN blocks. Four LAN switches and a /30 transit link complete the topology. Network IDs are not used as switch-port host addresses. |
| 10 | 64-79 | Routed LAN, wireless/DHCP/cloud and physical-lab procedure. Isolated upstream cloud DHCP settings follow the manual; this is not a production Internet design. |
| 11 | 80-92 | Full static/backup/host routes, return routes and RIPv2. Endpoint LAN masks are consistently /8; serial links /30. DCE clocking is assigned explicitly. |
| 12 | 93-95 | Complete TCP/UDP echo and turn-based chat authored for blank algorithm/output areas. TCP messages use length framing. |
| 13 | 96 | Complete raw ICMP program authored, with reply matching and real loopback evidence. |
| 14 | 97 | Complete Linux raw capture and portable decoder authored. Synthetic parser evidence is separated from live-capture claims. |
| 15 | 98-100 | Webalizer procedure/configuration and synthetic input. Webalizer execution is not claimed. |

Original listed titles/order are retained; typographic punctuation and broken PDF dashes are normalised. Additional practice exercises on page 5 are outside the 15 listed experiments.

Primary technical references used to check API/protocol semantics: [Python sockets](https://docs.python.org/3/library/socket.html), [RFC 792](https://www.rfc-editor.org/rfc/rfc792), [Nmap host discovery](https://nmap.org/book/man-host-discovery.html), [TShark manual](https://www.wireshark.org/docs/man-pages/tshark.html).
