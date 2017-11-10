import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
csvfile = csv.writer(open('nexb-license-requirements.csv', 'wb'))
csvfile.writerow("key","requirements")
page = "https://enterprise.dejacode.com/license_library/Demo/"
with open('nexb_license.csv', 'rb') as csvlicense:
        reader = csv.DictReader(csvlicense)
        for row in reader:
                key = row['key']
                url = page + key
                r =requests.get(url)
                soup = BeautifulSoup(r.content)
                headers = soup.find("div",{"id":"tab_license-requirements"}).findAll("div",{"class":"tag-True"})
                for item in headers:
                        header = item.find("strong").text
                        print key,",",header
                        csvfile.writerow([key,header])
