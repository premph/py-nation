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
    return soup

def content(url):
    para = dict()
    newurl = url
    newsoup = soupthis(newurl)
    content = newsoup.find("div",{"class":"content__article-body from-content-api js-article__body"})
    links =content.findAll("p")
    print(len(links))
    for k in range(len(links)):
        para[str(k)]=links[k]
    return para

def dictionary(results,result_size):
    
    for x in range(result_size):
        pp=dict()
        res = dict()
        res['sectionName']=results[x]['sectionName']
        res['webPublicationDate']=results[x]['webPublicationDate']
        res['webTitle']=results[x]['webTitle']
        res['webUrl']=results[x]['webUrl']
        res['pillarName']=results[x]['pillarName']
        res['type']=results[x]['type']
        master_res[str(x)]=res
        
        if (results[x]['type']=='article'):
            print('article')
            pp = content(results[x]['webUrl'])
            master_pp[str(x)]=pp
        
        else:
            print(results[x]['type'])
        print('------')
        
    return master_res,master_pp

def do():
    key = '20aa3bd8-063a-4088-9f68-8dc3b05cbc7c'
    search ='movies'
    order_by ='relevance'
    result_size = 2
    f_search = search.replace(' ','%20')
    url = 'https://content.guardianapis.com/search?order-by='+order_by+'&page-size='+str(result_size)+'&q='+f_search+'&api-key='+key
    
    
    
    data = json.loads(soupthis(url).prettify())
    
    results = data['response']['results']
    print('type of results',type(results))
    
    r,p = dictionary(results,result_size)
    
    
    print(r)
    print(p)
master_res = dict()
    
master_pp = dict()
do()

# -*- coding: utf-8 -*-

