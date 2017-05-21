#!/usr/bin/python3


from scapy.all import *

import time

class DashScanner():
    def __init__(self):
        self.last_check_time = time.time()
        self.MAC_dash_fairy = "ac:63:be:d4:7e:3d"
    def notify_hass(self):
        tnow = time.time()
        print("Dash probe received, last time was "+str(tnow-self.last_check_time)+" seconds ago")
        self.last_check_time = tnow;

    def arp_scan(self,pkt):
        if pkt.haslayer(ARP):
            if pkt[ARP].op == 1: #who-has (request)
                #print(pkt[ARP].hwsrc)
                if pkt[ARP].hwsrc == self.MAC_dash_fairy:
                    #print(pkt[ARP])
                    pkt.show()
                    #print("Probe from DASH")
                    self.notify_hass()






if __name__ == "__main__":
  dS = DashScanner()
  sniff(prn=dS.arp_scan,filter="arp",store=0,count=0)
