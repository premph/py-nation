# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 13:29:40 2018

@author: SPARTAN
"""

from bs4 import BeautifulSoup

import urllib.request
import json

def soupthis(url):
    
    webdata = urllib.request.urlopen(url)
    soup = BeautifulSoup(webdata,"html.parser")
    #val =soup.prettify()
    #print(type(val))
    return soup

def content(url):
    newurl = url
    newsoup = soupthis(newurl)
    content = newsoup.find("div",{"class":"content__article-body from-content-api js-article__body"})
    links =content.findAll("p")
    print(len(links))
    #for k in links:
       # print(k)
    return links



