import csv 
import re
from bs4 import BeautifulSoup
import sys
import requests
csvfile = csv.writer(open('nexb_license_information.csv', 'wb'))
csvfile.writerow(["key","name", "short_name", "guidance", "category", "license_type","license_profile","license_style","owner",
                  "SPDX_license_key","publication_year","keywords","special_obligations","license_text","homepage_url","text_urls","osi_url","faq_url","guidance_url","other_urls",
                  "owner_name","owner_homepage_url","owner_type","contact_information","alias","owner_notes"])
page = "https://enterprise.dejacode.com/license_library/Demo/"
with open('nexb_license.csv', 'rb') as csvlicense:
        reader = csv.DictReader(csvlicense)
        for row in reader:
                key = row['key']
                url = page + key
                r =requests.get(url)
                soup = BeautifulSoup(r.content)
                tab_essentials =soup.find("div",{"id":"tab_essentials"}).findAll("pre")
                key = tab_essentials[0].text.encode('ascii', 'ignore').decode('ascii')
                name = tab_essentials[1].text.encode('ascii', 'ignore').decode('ascii')
                short_name = tab_essentials[2].text.encode('ascii', 'ignore').decode('ascii')
                guidance = tab_essentials[3].text.encode('ascii', 'ignore').decode('ascii')
                category = tab_essentials[4].text.encode('ascii', 'ignore').decode('ascii')
                license_type = tab_essentials[5].text.encode('ascii', 'ignore').decode('ascii')
                license_profile= tab_essentials[6].text.encode('ascii', 'ignore').decode('ascii')
                license_style= tab_essentials[7].text.encode('ascii', 'ignore').decode('ascii')
                owner= tab_essentials[8].text.encode('ascii', 'ignore').decode('ascii')
                SPDX_license_key= tab_essentials[9].text.encode('ascii', 'ignore').decode('ascii')
                publication_year= tab_essentials[10].text.encode('ascii', 'ignore').decode('ascii')
                keywords= tab_essentials[11].text.encode('ascii', 'ignore').decode('ascii')
                special_obligations= tab_essentials[12].text.encode('ascii', 'ignore').decode('ascii')
                #URN= tab_essentials[13].text
                #dataspace = tab_essentials[14].text
                license_text = soup.find("div",{"id":"tab_license-text"}).findAll("pre")[0].text
                tab_url = soup.find("div",{"id":"tab_urls"}).findAll("pre")
                homepage_url = tab_url[0].text.encode('ascii', 'ignore').decode('ascii')
                text_urls = tab_url[1].text.encode('ascii', 'ignore').decode('ascii')
                osi_url = tab_url[2].text.encode('ascii', 'ignore').decode('ascii')
                faq_url= tab_url[3].text.encode('ascii', 'ignore').decode('ascii')
                guidance_url= tab_url[4].text.encode('ascii', 'ignore').decode('ascii')
                other_urls = tab_url[5].text.encode('ascii', 'ignore').decode('ascii')
                #print homepage_url,text_urls,osi_url,faq_url,guidance_url,other_urls
                tab_owner = soup.find("div",{"id":"tab_owner"}).findAll("pre")
                owner_name = tab_owner[0].text.encode('ascii', 'ignore').decode('ascii')
                owner_homepage_url= tab_owner[1].text.encode('ascii', 'ignore').decode('ascii')
                owner_type= tab_owner[2].text.encode('ascii', 'ignore').decode('ascii')
                contact_information= tab_owner[3].text.encode('ascii', 'ignore').decode('ascii')
                alias= tab_owner[4].text.encode('ascii', 'ignore').decode('ascii')
                owner_notes= tab_owner[5].text.encode('ascii', 'ignore').decode('ascii')
                #print owner_name,owner_homepage_url,owner_type,contact_information,alias,owner_notes
                csvfile.writerow([key,name, short_name, guidance, category, license_type,license_profile,license_style,owner,SPDX_license_key,publication_year,keywords,special_obligations,license_text,
                  homepage_url,text_urls,osi_url,faq_url,guidance_url,other_urls,owner_name,owner_homepage_url,owner_type,contact_information,alias,owner_notes])

