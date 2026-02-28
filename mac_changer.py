#!/usr/bin/env python3
import subprocess
import optparse
import re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac_address", dest="mac_addr", help="Change mac address")
    (options , argument) =  parser.parse_args()
    if not options.interface:
        parser.error("please specify interface.Try --help for more")
    elif not options.mac_addr:
        parser.error("please specify mac_addr.Try --help for more")
    return options

def change_mac(interface , mac_addr):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_search_result = re.search(rb"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    print(mac_addr_search_result.group(0))


# subprocess.call("ifconfig" + interface + "down",shell=True)
# subprocess.call("ifconfig" + interface + "hw ether" + mac_addr,shell=True)
# subprocess.call("ifconfig" + interface + "up",shell=True)
options = get_argument()
#change_mac(options.interface,options.mac_addr)

get_current_mac(options.interface)
