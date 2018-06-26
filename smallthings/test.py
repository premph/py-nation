# -*- coding: utf-8 -*-

from aylienapiclient import textapi
client = textapi.Client("5428d0d9", "6df5f167c1dadde3815ffce90b8f3534")
text ='you are cruel'
d = dict()
a=['how are you','are you hurt','wonderful speech','']
for x  in range(len(a)):
    d[str(x)] = client.Sentiment(a[x])
    

#print(d)

for x,y in d.items():
    print(x,' ',y)