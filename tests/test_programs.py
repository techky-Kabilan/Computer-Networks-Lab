import importlib.util
import socket
import struct
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

h = load('hamming', 'Exercise_06/hamming.py')
w = load('sliding', 'Exercise_07/sliding_window.py')
net = load('sockets_lab', 'Exercise_12/sockets_lab.py')
ping = load('raw_ping', 'Exercise_13/ping.py')
sniffer = load('sniffer', 'Exercise_14/sniffer.py')

def ipv4(payload, protocol=1, source='10.1.1.2', destination='10.1.1.1',
         options=b'', fragment=0):
    ihl = 20 + len(options)
    assert ihl % 4 == 0
    header = struct.pack('!BBHHHBBH4s4s', 0x40 | ihl//4, 0,
                         ihl + len(payload), 1, fragment, 64, protocol, 0,
                         socket.inet_aton(source), socket.inet_aton(destination)) + options
    check = ping.checksum(header)
    header = header[:10] + struct.pack('!H', check) + header[12:]
    return header + payload

def echo_reply(identifier=123, sequence=4, payload=b'hello'):
    header = struct.pack('!BBHHH', 0, 0, 0, identifier, sequence)
    return struct.pack('!BBHHH', 0, 0, ping.checksum(header+payload),
                       identifier, sequence) + payload

def ethernet(payload, kind=0x0800):
    return bytes.fromhex('020000000001020000000002') + struct.pack('!H', kind) + payload

class HammingTests(unittest.TestCase):
    def test_all_bytes_and_all_single_bit_errors(self):
        for byte in range(256):
            block = h.encode_byte(byte)
            self.assertEqual(h.decode_block(block), (byte, 0))
            for i in range(12):
                bad = block[:i] + str(1-int(block[i])) + block[i+1:]
                self.assertEqual(h.decode_block(bad), (byte, i+1))
    def test_unicode_and_empty_channel(self):
        with tempfile.TemporaryDirectory() as d:
            channel = Path(d)/'channel'
            for text in ('', 'Computer Networks', 'Tamil: \u0ba4\u0bae\u0bbf\u0bb4\u0bcd'):
                h.send(text, channel)
                if text:
                    h.flip(channel, 1, 6)
                self.assertEqual(h.receive(channel)[0], text)
    def test_invalid_blocks(self):
        for value in ('000', 'x'*12):
            with self.assertRaises(ValueError): h.decode_block(value)

class WindowTests(unittest.TestCase):
    def test_windows_and_errors(self):
        with tempfile.TemporaryDirectory() as d:
            for size in (1, 3, 20):
                output, events = w.simulate('NETWORK', size, d, 4,
                                           bad_ack_once=True, timeout_once=True)
                self.assertEqual(output, 'NETWORK')
                self.assertTrue(any('NACK' in e for e in events))
                self.assertTrue(any('INVALID' in e for e in events))
                self.assertTrue(any('TIMEOUT' in e for e in events))
    def test_empty_and_invalid(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(w.simulate('', 3, d)[0], '')
            with self.assertRaises(ValueError): w.simulate('A', 0, d)

class SocketTests(unittest.TestCase):
    def test_tcp_and_udp_echo(self):
        values = ['', 'Hello CN', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd', 'bye']
        for proto in ('tcp', 'udp'):
            self.assertEqual(net.demo(proto, 'echo', values), values)
    def test_tcp_message_larger_than_recv_buffer(self):
        text = 'network'*10000
        self.assertEqual(net.demo('tcp', 'echo', [text, 'bye']), [text, 'bye'])
    def test_chat_both_protocols(self):
        for proto in ('tcp', 'udp'):
            self.assertEqual(net.demo(proto, 'chat', ['Hello', 'bye']),
                             ['Server received: Hello', 'bye'])

class PacketTests(unittest.TestCase):
    def test_checksum_known_vector_and_request(self):
        self.assertEqual(ping.checksum(bytes.fromhex('0001f203f4f5f6f7')), 0x220d)
        self.assertEqual(ping.checksum(ping.request(123, 4)), 0)
    def test_reply_with_options_and_matching(self):
        for options in (b'', b'\x01\x01\x01\x01'):
            packet = ipv4(echo_reply(), options=options)
            self.assertEqual(ping.parse_reply(packet, '10.1.1.2', 123, 4)['payload'], b'hello')
            self.assertIsNone(ping.parse_reply(packet, '10.1.1.2', 124, 4))
            self.assertIsNone(ping.parse_reply(packet[:-1], '10.1.1.2', 123, 4))
    def test_sniffer_icmp_udp_tcp(self):
        icmp = sniffer.decode_frame(ethernet(ipv4(echo_reply())))
        self.assertEqual(icmp['icmp_type'], 0)
        udp = struct.pack('!HHHH', 1234, 53, 8, 0)
        self.assertEqual(sniffer.decode_frame(ethernet(ipv4(udp,17)))['destination_port'], 53)
        tcp = struct.pack('!HHIIBBHHH', 1234, 80, 1, 2, 0x50, 0x12, 4096, 0, 0)
        self.assertEqual(sniffer.decode_frame(ethernet(ipv4(tcp,6)))['flags'], 0x12)
    def test_fragments_and_truncation(self):
        frame = ethernet(ipv4(b'abc', 17, fragment=1))
        decoded = sniffer.decode_frame(frame)
        self.assertTrue(decoded['fragmented'])
        self.assertNotIn('source_port', decoded)
        with self.assertRaises(ValueError): sniffer.decode_frame(b'abc')
        with self.assertRaises(ValueError): sniffer.decode_frame(ethernet(ipv4(b'a',17)))
    def test_vlan_and_arp(self):
        tagged = ethernet(struct.pack('!HH',7,0x0800)+ipv4(echo_reply()),0x8100)
        self.assertEqual(sniffer.decode_frame(tagged)['vlan'], 7)
        self.assertEqual(sniffer.decode_frame(ethernet(b'',0x0806))['protocol'], 'ARP')

if __name__ == '__main__': unittest.main(verbosity=2)
