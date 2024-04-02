import scapy.all as scapy


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    arp_req_broadcast = broadcast/arp_req
    answerd_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    print("answered_list: ", answerd_list.summary())

scan("10.0.0.1/24")
