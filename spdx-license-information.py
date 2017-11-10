import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
import codecs
csvfile = csv.writer(open('nexb-SPDX-license-info.csv', 'wb'))
csvfile.writerow(["key","SPDX_license_key","SPDX_fullname","SPDX_source_url","SPDX_notes"])
page = "https://enterprise.dejacode.com/license_library/Demo/"
with open('nexb_license.csv', 'rb') as csvlicense:
        reader = csv.DictReader(csvlicense)
        for row in reader:
                key = row['key']
                url = page + key
                r =requests.get(url)
                soup = BeautifulSoup(r.content)
                tab = soup.find("ul",{"id":"details_tab"}).find("a",href="#tab_spdx")
                if  tab:
                        tab_spdx =soup.find("div",{"id":"tab_spdx"}).find_all("pre")
                        SPDX_license_key= tab_spdx[0].text.encode('ascii', 'ignore').decode('ascii')
                        SPDX_fullname = tab_spdx[1].text.encode('ascii', 'ignore').decode('ascii')
                        SPDX_source_url= tab_spdx[2].text.encode('ascii', 'ignore').decode('ascii')
                        SPDX_notes = tab_spdx[3].text.encode('ascii', 'ignore').decode('ascii')
                       # SPDX_license_text = tab_spdx[4].text.encode('ascii', 'ignore').decode('ascii')
                       # license text is too long
                        print SPDX_license_key,SPDX_fullname,SPDX_source_url,SPDX_notes #,SPDX_license_text
                        csvfile.writerow([key,SPDX_license_key,SPDX_fullname,SPDX_notes])

