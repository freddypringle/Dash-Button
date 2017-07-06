from scapy.all import *
print "Ready"
def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        print "HWSRC: " + pkt[ARP].hwsrc + ", PSRC: " + pkt[ARP].psrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)