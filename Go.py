import winsound
from scapy.all import *

from dbhelper import DBHelper
db = DBHelper()
db.setup()

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice").Speak

print "Ready"
def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].hwsrc == '50:f5:da:fe:a4:a9': # Huggies
            print "Pushed Button"
            speak("To do list:")
            items = db.get_items()
            for item in items: speak(item)            

print sniff(prn=arp_display, filter="arp", store=0, count=0)