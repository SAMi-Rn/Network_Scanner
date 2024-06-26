import scapy.all as scapy
import requests
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP Range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP/IP Range, use --help for more info.")
    return options


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.show())

    devices_list = []
    for answer in answered_list:
        dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc, "vendor": vendor_lookup(answer[1].hwsrc)}
        devices_list.append(dict)
    return devices_list


def vendor_lookup(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except requests.RequestException:
        return "Lookup Failed"


def print_devices(devices_list):
    print("IP Address\t\tMAC Address\t\t\t\tVendor\n---------------------------------------------------")
    for device in devices_list:
        print(device["ip"] + "\t\t" + device["mac"] + "\t\t" + device["vendor"])


options = get_arguments()
result = scan(options.target)
print_devices(result)
