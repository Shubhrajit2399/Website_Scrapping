# Website_Scrapping
This project is regarding a web-scrapping using random non traceable IPs and filter, format and store the website into csv file.

In this project we have used the below website to scrap:
https://books.toscrape.com/index.html

*Here free random proxy IPs are used:
https://free-proxy-list.net/en/

**In real-world scrapping cases we use paid proxies. Oxylab is a good coice for that- https://oxylabs.io/
***For checking responses you can use random json address- https://www.ipify.org/

****If you are using paid proxy in that case response code can be in more easy format:

<<<

import requests

url="https://api64.ipify.org?format=json"

proxies={
        "http" : "<<Proxy from Oxylab>>",
        "https" : "<<Proxy from Oxylab>>"
    }

r=requests.get(url,proxies=proxies)
print(r.json())

>>>
