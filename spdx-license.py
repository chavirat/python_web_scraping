import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
csvfile = csv.writer(open('spdx_license.csv', 'wb'))
csvfile.writerow(["SPDX_license_key"])
url = "http://spdx.org/licenses/" 
r =requests.get(url)
soup = BeautifulSoup(r.content)
table = soup.find('table',{'class':'sortable'})
names = table.find_all('code',{'property':'spdx:licenseId'})
osi_approveds = table.find_all('td',{'align':'center'})
for item in names:
        name = item.text
        csvfile.writerow([name])
