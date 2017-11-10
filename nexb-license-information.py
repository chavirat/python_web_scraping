import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
import codecs
csvfile = csv.writer(open('nexb-license-information.csv', 'wb'))
csvfile.writerow(["key","name", "short_name", "guidance", "category", "license_type","license_profile","license_style","owner",
                  "SPDX_license_key","publication_year","keywords","special_obligations","homepage_url","text_urls","osi_url","faq_url","guidance_url","other_urls",
                  "owner_name","owner_homepage_url","owner_type","contact_information","alias","owner_notes"])
page = "https://enterprise.dejacode.com/license_library/Demo/"
with open('nexb_license.csv', 'rb') as csvlicense:
        reader = csv.DictReader(csvlicense)
        for row in reader:
                key = row['key']
                url = page + key
                r =requests.get(url)
                soup = BeautifulSoup(r.content)
                
                tab_url = soup.find("div",{"id":"tab_urls"}).findAll("pre")
                homepage_url = tab_url[0].text.encode('ascii', 'ignore').decode('ascii')
                text_urls = tab_url[1].text.encode('ascii', 'ignore').decode('ascii')
                osi_url = tab_url[2].text.encode('ascii', 'ignore').decode('ascii')
                faq_url= tab_url[3].text.encode('ascii', 'ignore').decode('ascii')
                guidance_url= tab_url[4].text.encode('ascii', 'ignore').decode('ascii')
                other_urls = tab_url[5].text.encode('ascii', 'ignore').decode('ascii')
                
                tab_owner = soup.find("div",{"id":"tab_owner"}).findAll("pre")
                owner_name = tab_owner[0].text.encode('ascii', 'ignore').decode('ascii')
                owner_homepage_url= tab_owner[1].text.encode('ascii', 'ignore').decode('ascii')
                owner_type= tab_owner[2].text.encode('ascii', 'ignore').decode('ascii')
                contact_information= tab_owner[3].text.encode('ascii', 'ignore').decode('ascii')
                alias= tab_owner[4].text.encode('ascii', 'ignore').decode('ascii')
                owner_notes= tab_owner[5].text.encode('ascii', 'ignore').decode('ascii')
                
                tab_essentials =soup.find("div",{"id":"tab_essentials"}).findAll("dt")
                for item in tab_essentials:
                    if "Name" in item.text:
                        name = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Short name" in item.text:
                        short_name = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Guidance" in item.text:
                        guidance = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Category" in item.text:
                        category = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "License type" in item.text:
                        license_type = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "License profile" in item.text:
                        license_profile = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "License style" in item.text:
                        license_style = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Owner" in item.text:
                        owner = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "SPDX license key" in item.text:
                        SPDX_license_key = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Publication year" in item.text:
                        publication_year = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Keywords" in item.text:
                        keywords = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "Special obligations" in item.text:
                        special_obligations = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                    if "URN" in item.text:
                        URN = item.findNext("pre").text.encode('ascii', 'ignore').decode('ascii')
                        
                        print key,name, short_name, guidance, category, license_type,license_profile,license_style,owner,SPDX_license_key,publication_year,keywords,special_obligations,
                        homepage_url,text_urls,osi_url,faq_url,guidance_url,other_urls,owner_name,owner_homepage_url,owner_type,contact_information,alias,owner_notes
                        
                        csvfile.writerow([key,name, short_name, guidance, category, license_type,license_profile,license_style,owner,SPDX_license_key,publication_year,keywords,special_obligations,
                                          homepage_url,text_urls,osi_url,faq_url,guidance_url,other_urls,owner_name,owner_homepage_url,owner_type,contact_information,alias,owner_notes])

