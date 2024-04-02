import scapy.all as scapy


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    arp_req_broadcast = broadcast/arp_req
    arp_req_broadcast.show()

scan("10.0.0.1/24")
