import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
#csvobligations = csv.writer(open('obligations.csv', 'wb'))
#csvrestrictions = csv.writer(open('restrictions.csv', 'wb'))
#csvpolicies = csv.writer(open('policies.csv', 'wb'))
#csvinformation = csv.writer(open('information.csv', 'wb'))
csvrequirements = csv.writer(open('nexb_requirements.csv', 'wb'))
url = "https://enterprise.dejacode.com/license_library/Demo/glide/"
r =requests.get(url)
soup = BeautifulSoup(r.content)
csvrequirements.writerow(["name","description","type"])
if "Obligations" in soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[0].text:
        headers = soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[0].findNext("div",{"class":"well well-sm"}).findAll("div")
        for item in headers:
                header = item.find("strong").text
                content = item.find("p").text
                csvrequirements.writerow([ header, content,"obligation"])
if "Restrictions" in soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[1].text:
        headers = soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[1].findNext("div",{"class":"well well-sm"}).findAll("div")
        for item in headers:
                header = item.find("strong").text
                content = item.find("p").text
                csvrequirements.writerow([ header, content,"restrictions"])           
if "Policies" in soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[2].text:
        headers = soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[2].findNext("div",{"class":"well well-sm"}).findAll("div")
        for item in headers:
                header = item.find("strong").text
                content = item.find("p").text
                csvrequirements.writerow([ header, content,"policies"])   
if "Information" in soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[3].text:
        headers = soup.find("div",{"id":"tab_license-requirements"}).findAll("h2")[3].findNext("div",{"class":"well well-sm"}).findAll("div")
        for item in headers:
                header = item.find("strong").text
                content = item.find("p").text
                csvrequirements.writerow([ header, content,"information"])          
