import scapy.all as scapy


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    for answer in answered_list:
        print("IP Address: " + answer[1].psrc)
        print("MAC Address: " + answer[1].hwsrc)
        print("---------------------------------------------------")

scan("10.0.0.1/24")
