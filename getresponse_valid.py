#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 18:01:57 2025

@author: shubhrajit
"""

import requests

with open("responsive_ip.txt","r") as f:
    proxies= f.read().split("\n")
    
    
sites_to_check=[]
for i in range(1,51):
    a=(f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html")
    sites_to_check.append(a)

counter=0
i=0
for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}-{i}")
        res=requests.get(site, proxies={"http" : proxies[counter],
                                        "https" : proxies[counter]})
        print(res.status_code)
        with open(f"scrapped_files/webpage{i}.html","w") as w:
            w.write(res.text)
            print(f"Page-{i} Downloaded successfully at counter {counter}")
            i+=1
    except:
        print("Failed")
    finally:
        if (counter<len(proxies)-1):
            counter+=1
        else:
            counter=0
       