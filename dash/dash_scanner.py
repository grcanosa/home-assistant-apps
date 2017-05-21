#!/usr/bin/python3


from scapy.all import *



def notify_hass():
  

def arp_scan(pkt):
    if pkt.haslayer(ARP):
        if pkt[ARP].op == 1: #who-has (request)
            if pkt[ARP].hwsrc == "c4:a3:66:d3:5b:1e":
              print("Probe from DASH")


sniff(prn=arp_scan,filter="arp",store=0,count=0)                      