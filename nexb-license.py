import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
#filename = raw_input("please enter the output file name (.csv): ")
#filename = str(filename)
csvfile = csv.writer(open('nexb_license.csv', 'wb'))
#csvfile.writerow(["license_id","license_name"])
for page in range(1,12):
        url = "https://enterprise.dejacode.com/license_library/?q=&o=name&selected_ids=&selected_facets=%7B%7D&ot=asc&page=" + str(page)
        r =requests.get(url)
        soup = BeautifulSoup(r.content)
        links = soup.find_all('a', href=re.compile('/license_library/Demo/'))
        for link in links:             
                license_link = link.get("href")
                if not 'owner' in license_link:
                        #print license_link
                        license_name = link.text
                        #print license_name
                        nme = license_link.replace('/license_library/Demo/','')
                        license_id = nme.replace ('/','')
                        print license_id
                        csvfile.writerow([license_id,license_name])
