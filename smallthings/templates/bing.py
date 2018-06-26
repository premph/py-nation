# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:29:40 2018

@author: SPARTAN
"""

from bs4 import BeautifulSoup
import requests

para ={'search?q':'pizza'}

search =input('Enter something')
param={'q':search}
r = requests.get("https://www.bing.com/search?",params=param)


soup=BeautifulSoup(r.text,"html.parser")

#find all a tag and list their values

results = soup.find("ol",{"id":"b_results"}) 
links =results.findAll("li",{"class":"b_algo"})

for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]
    if(item_text and item_href):
        print(item_text)
        print(item_href)
        #print("Parent ",item.find("a").parent)
        print("Summary ",item.find("a").parent.parent.find('p').text)
        print("")
