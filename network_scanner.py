#!/usr/bin/env python3

import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  #pdst is a field
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
   # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)
    # print(answered_list.summary())
    # scapy.ls(scapy.ARP())
    # scapy.arping(ip)
    client_list = []
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]
    for element in answered_list:
        client_dict = {"Ip":element[1].psrc,"Mac":element[1].hwsrc}
        client_list.append(client_dict)
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return client_list

def print_result(result_list):
    print("IP\t\t\tMac_Address\n----------------------------------------------")
    for client in result_list:
        print(client["Ip"] + "\t\t" + client["Mac"])


print_result(scan("192.168.43.1/24")) 
