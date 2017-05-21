#!/usr/bin/python3


from scapy.all import *

import time

class DashScanner():
    def __init__(self):
        self.last_check_time = time.time()
    def notify_hass():
        tnow = time.time()
        print("Dash probe received, last time was "+str(tnow-self.last_check_time)+" seconds ago")
        self.last_check_time = tnow;

    def arp_scan(self,pkt):
        if pkt.haslayer(ARP):
            if pkt[ARP].op == 1: #who-has (request)
                if pkt[ARP].hwsrc == "c4:a3:66:d3:5b:1e":
                    #print("Probe from DASH")
                    self.notify_hass()






if name == "__main__":
  dS = DashScanner()
  sniff(prn=ds.arp_scan,filter="arp",store=0,count=0)
