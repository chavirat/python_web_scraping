#from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.poolmanager import PoolManager
#import ssl

#class MyAdapter(HTTPAdapter):
#    def init_poolmanager(self, connections, maxsize, block=False):
#        self.poolmanager = PoolManager(num_pools=connections,
#                                       maxsize=maxsize,
#                                       block=block,
#                                       ssl_version=ssl.PROTOCOL_TLSv1)
import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
import ssl

input = input.replace("!web", "")      
url = "https://tldrlegal.com/license/sleepycat-license" + input
req = urllib2.Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
info = urllib2.urlopen(req, context=gcontext).read()
Message.Chat.SendMessage ("" + info)
#r = s.mount('https://tldrlegal.com/license/sleepycat-license', MyAdapter())
#filename = raw_input("please enter the output file name (.csv): ")
#filename = str(filename)
#csvfile = csv.writer(open('tldr_license.csv', 'wb'))
#csvfile.writerow(["license_id","license_name"])
#for page in range(1,12):
#url = "https://tldrlegal.com/users/kevin"
#r =requests.get('https://tldrlegal.com/license/sleepycat-license')
#r = requests.get('https://tldrlegal.com/account/dashboard/#summary')
#s = requests.Session()
#print s
#soup = BeautifulSoup(r.content)
#links = soup.find_all('a')
#for link in links:             
 #       license_link = link.get("href")
        #if not 'owner' in license_link:
  #      print license_link
  #      license_name = link.text
   #     print license_name
        #csvfile.writerow([license_id,license_name])
