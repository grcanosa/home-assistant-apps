#!/usr/bin/python3


from scapy.all import *

import time
import requests
import json
import random
import sys




class DashScanner(filename=None,password=""):
    def __init__(self):
        self.last_check_time = time.time()
        self.url='http://192.168.1.98:8123/api/services/notify/grcanosabot'
        self.headers={'x-ha-access': password, 'content-type': 'application/json'}
        self.data={'title': 'Fairy te dice:', 'message': 'message'}
        self.load_from_file(filename)
        self.sentences = ["Te quiero"]

    def load_from_file(self,filename):
        with open(filename) as f:
            for l in f:
                l = l.strip();
                self.sentences.append(l)


    def notify_hass(self):
        self.data["message"] = random.choice(self.sentences)
        requests.post(self.url,headers=self.headers,json=self.data)


    def arp_scan(self,pkt):
        if pkt.haslayer(ARP):
            if pkt[ARP].op == 1: #who-has (request)
                if pkt[ARP].hwsrc == "c4:a3:66:d3:5b:1e":
                    #print("Probe from DASH")
                    tnow = time.time()
                    #print("Dash probe received, last time was "+str(tnow-self.last_check_time)+" seconds ago")
                    if tnow-self.last_check_time > 9:
                        self.notify_hass();
                    self.last_check_time = tnow;



if __name__ == "__main__":
  dS = DashScanner("piropos.txt",sys.argv[1])
  sniff(prn=dS.arp_scan,filter="arp",store=0,count=0)
