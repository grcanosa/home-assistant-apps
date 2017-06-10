#!/usr/bin/python3


from scapy.all import *

import time
import requests
import json
import random
import sys




class DashScanner():
    def __init__(self,filename=None,password=""):
        self.last_check_time = time.time()
        self.urlGR='http://192.168.1.100:8123/api/services/notify/bot_to_grcanosa'
        self.urlSA='http://192.168.1.100:8123/api/services/notify/bot_to_sara'
        self.headers={'x-ha-access': password, 'content-type': 'application/json'}
        self.data={'title': '<FAIRY>', 'message': ' Starting...'}
        self.sentences = ["Te quiero"]
        self.load_from_file(filename)
        requests.post(self.urlGR,headers=self.headers,json=self.data)

    def load_from_file(self,filename):
        with open(filename) as f:
            for l in f:
                l = l.strip();
                self.sentences.append(l)


    def notify_hass(self):
        self.data["message"] = random.choice(self.sentences)
        requests.post(self.urlGR,headers=self.headers,json=self.data)


    def arp_scan(self,pkt):
        if pkt.haslayer(ARP):
            if pkt[ARP].op == 1: #who-has (request)
                if pkt[ARP].hwsrc == "ac:63:be:d4:7e:3d":
                    #print("Probe from DASH")
                    tnow = time.time()
                    #print("Dash probe received, last time was "+str(tnow-self.last_check_time)+" seconds ago")
                    #print(pkt[ARP])
                    if tnow-self.last_check_time > 15:
                        self.notify_hass();
                        self.last_check_time = tnow;



if __name__ == "__main__":
  #print(sys.argv)
  dS = DashScanner(sys.argv[2],sys.argv[1])
  sniff(prn=dS.arp_scan,filter="arp",store=0,count=0)
