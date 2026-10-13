import importlib.util, json, subprocess, sys, tempfile, threading, struct, socket, hashlib
from pathlib import Path
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

root=Path(__file__).resolve().parents[1]
def module(n,name):
 spec=importlib.util.spec_from_file_location(name,root/f'Exercise_{n:02d}/{name}.py')
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
ftp=module(6,'ftp_scanner')
results=[]
with tempfile.TemporaryDirectory() as home:
 for enabled in [True,False]:
  authorizer=DummyAuthorizer()
  if enabled:authorizer.add_anonymous(home,perm='elr')
  else:authorizer.add_user('student','lab',home,perm='elr')
  class Handler(FTPHandler):pass
  Handler.authorizer=authorizer;Handler.auth_failed_timeout=0
  server=FTPServer(('127.0.0.1',0),Handler)
  port=server.socket.getsockname()[1]
  worker=threading.Thread(target=server.serve_forever,kwargs={'timeout':.1});worker.start()
  try:
   value=ftp.check('127.0.0.1',port);assert value['anonymous'] is enabled
   results.append(json.dumps(value,sort_keys=True))
  finally:server.close_all();worker.join()
(root/'Exercise_06/outputs/actual.txt').write_text('Actual localhost FTP tests (ephemeral ports):\n'+'\n'.join(results)+'\n')
for n,name in [(7,'calculator'),(8,'reverse_shell')]:
 result=subprocess.run([sys.executable,str(root/f'Exercise_{n:02d}/{name}.py'),'demo'],capture_output=True,text=True,timeout=30,check=True)
 (root/f'Exercise_{n:02d}/outputs/actual.txt').write_text('Actual localhost demonstration:\n'+result.stdout)
 if n==7:assert all(x in result.stdout for x in ['16','8','48','3.0','fault'])
 else:assert 'Python' in result.stdout and 'Session closed' in result.stdout
sniffer=module(4,'sniffer');frame=bytes.fromhex((root/'Exercise_04/outputs/fixture.hex').read_text())
assert sniffer.decode_frame(frame)['protocol']=='ICMP'
ping=module(5,'ping');assert ping.checksum(ping.request(42,1))==0
for n in [4,5,6,7,8]:
 for file in (root/f'Exercise_{n:02d}').glob('*.py'):compile(file.read_text(),str(file),'exec')
# Independent synthetic PCAP: one complete IPv4/UDP Ethernet packet.
payload=b'CN forensic fixture';udp=struct.pack('!HHHH',12345,9999,8+len(payload),0)+payload
ip=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(udp),1,0,64,17,0,socket.inet_aton('192.0.2.10'),socket.inet_aton('192.0.2.20'))
ip=ip[:10]+struct.pack('!H',ping.checksum(ip))+ip[12:]
packet=bytes.fromhex('00112233445566778899aabb0800')+ip+udp
pcap=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1)+struct.pack('<IIII',1700000000,0,len(packet),len(packet))+packet
(root/'Exercise_13/sample.pcap').write_bytes(pcap)
decoded=sniffer.decode_frame(packet)
assert decoded['source_ip']=='192.0.2.10' and decoded['destination_port']==9999
(root/'Exercise_13/outputs/actual.txt').write_text('Actual independent fixture verification; NOT PcapXray output.\n'+json.dumps(decoded,indent=2,sort_keys=True)+'\nPCAP: 1 Ethernet/IPv4/UDP packet; no live traffic.\n')
(root/'verification').mkdir(exist_ok=True)
(root/'verification/checks.txt').write_text('PASS: anonymous FTP login accepted and rejected using local servers\nPASS: XML-RPC add/subtract/multiply/divide and zero-division fault\nPASS: localhost reverse-shell command and exit\nPASS: raw-sniffer fixture decode\nPASS: ICMP Echo checksum\nPASS: synthetic PCAP structure/endpoints\nPASS: syntax compilation of supplied Python programs\nPreviously captured localhost Wireshark output retained for Exercise 14.\nPacket Tracer, physical crimping, Nmap/TryHackMe, PcapXray GUI and Webalizer not executed.\n')
items=json.loads((root/'tools/experiment_data.json').read_text())
rows=[]
for item in items:
 n=item['number'];directory=root/f'Exercise_{n:02d}'
 text=f'# Exercise {n:02d}: {item["title"]}\n\n[Open the PDF](CN_Exercise_{n:02d}.pdf)\n\n## Aim\n\n{item["aim"]}\n\n## Requirements\n\n{item["requirements"]}\n\n## Procedure / algorithm\n\n'
 text+='\n'.join(f'{i}. {step}' for i,step in enumerate(item['procedure'],1))+'\n\n## Complete code / configuration\n\n'
 for path in item['files']:
  p=root/path;text+=f'### [{p.name}]({p.relative_to(directory).as_posix()})\n\n```\n{p.read_text()}\n```\n\n'
 if n==13:text+='[Download the synthetic capture](sample.pcap)\n\n'
 if item.get('run'):text+='## Run\n\n```\n'+'\n'.join(item['run'])+'\n```\n\n'
 actual=directory/'outputs/actual.txt'
 text+='## Actual output\n\n'+('```\n'+actual.read_text()+'\n```' if actual.exists() else 'Not executed in the required lab/tool environment.')+'\n\n'
 text+=f'## Expected output\n\n{item["expected"]}\n\n## Observations\n\n{item["observations"]}\n\n## Result\n\n{item["result"]}\n'
 (directory/'README.md').write_text(text,encoding='utf-8')
 rows.append(f'| {n} | {item["title"]} | [PDF](Exercise_{n:02d}/CN_Exercise_{n:02d}.pdf) |')
 (directory/'outputs/expected.txt').write_text('EXPECTED OUTPUT — not an execution record\n'+item['expected']+'\n',encoding='utf-8')
(root/'README.md').write_text('# CS23532 Computer Networks — Document-Matched Record Exercises\n\nThis set follows the exact 15 titles in Computer Networks Record.docx. It is separate from the previously published manual-based exercises and the handwritten observation record. Each folder includes a complete PDF, source/configuration, procedure, output and result. Actual checks and expected lab outcomes are explicitly separated.\n\n| Exercise | Original record title | Record |\n|---|---|---|\n'+'\n'.join(rows)+'\n\n## Verification\n\nSee [checks](verification/checks.txt). Program tests use localhost and synthetic fixtures. Packet Tracer configurations, physical labs, TryHackMe, PcapXray GUI and Webalizer require their lab environments.\n\n## References\n\n- [Python ftplib](https://docs.python.org/3/library/ftplib.html)\n- [Python XML-RPC server](https://docs.python.org/3/library/xmlrpc.server.html)\n- [Cisco NAT configuration](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html)\n- [PcapXray setup and usage](https://github.com/srixivas/PcapXray)\n\nNo student details, dates or signatures are included in this project.\n',encoding='utf-8')
print('All matching-program checks passed')
