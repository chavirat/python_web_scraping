#web-scraping from http://spdx.org/licenses
import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
import codecs
csvfile = csv.writer(open('SPDX-license-info.csv', 'wb'))
csvfile.writerow(["SPDX_license_key","SPDX_fullname","SPDX_source_url","SPDX_notes","license_header"])#,"license_text"])
with open('spdx_license.csv', 'rb') as csvsdpx:
        reader = csv.DictReader(csvsdpx)
        for row in reader:
                key = row['SPDX_license_key']
                url = "http://spdx.org/licenses/"+str(key)+".html"
                r =requests.get(url)
                soup = BeautifulSoup(r.content)
                names = soup.find_all("h2")
                for name in names:
                    if "Short identifier" in name:
                        spdx_key = name.findNext("code").text.replace("&quot;"," ").encode('ascii', 'ignore').decode('ascii')
                        print spdx_key
                    if "Full name" in name:    
                        spdx_name = name.findNext("code").text.replace("&quot;"," ").encode('ascii', 'ignore').decode('ascii')
                        print spdx_name
                    if "Other web pages for this license" in name:
                        links = name.findNext("ul").text.replace("&quot;"," ").encode('ascii', 'ignore').decode('ascii')
                notes = soup.find("h2",{"id":"notes"}).findNext("p").text.replace("&quot;"," ").encode('ascii', 'ignore').decode('ascii')
                #licenseText = soup.find("h2",{"id":"licenseText"}).findNext("div").text.replace("&quot;"," ").encode('ascii', 'ignore').decode('ascii')
                #too long
                licenseHeader = soup.find("h2",{"id":"licenseHeader"}).findNext("div").text.replace("&quot;"," ").encode('ascii', 'ignore').decode('ascii')
                csvfile.writerow([spdx_key,spdx_name,links,notes,licenseHeader])#,licenseText])

