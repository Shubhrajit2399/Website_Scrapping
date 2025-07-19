#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 17:27:44 2025

@author: shubhrajit
"""

import threading
import queue
import requests

q=queue.Queue()
valid_proxies=[]

with open("proxy_list.txt","r") as f:
    proxies=f.read().split("\n")
    for p in proxies:
        q.put(p)
        
def check_proxies():
    global g
    while not q.empty():
        proxy=q.get()
        try:
            res = requests.get("https://api64.ipify.org?format=json", 
                               proxies={"http" : proxy,
                                        "https" : proxy})
            
        except:
            continue
        
        if res.status_code==200:
            print(proxy)
            
for _ in range(10):
    threading.Thread(target=check_proxies).start()