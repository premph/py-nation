# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from aylienapiclient import textapi

client = textapi.Client("5428d0d9", "6df5f167c1dadde3815ffce90b8f3534")
f = open('reviews.txt','r')
data = f.read()
f.close()
l = data.split('0')
le = len(l)-1
dd= dict()
for x in range(le):
    dd[str(x)]=client.Sentiment(l[x])
ll =[]
pol=[]
sub=[]
#subjectivity_confidence
#print(dd)
for x in dd.values():
    for m,n in x.items():
        if(m=='polarity' or m=='subjectivity'):
            ll.append(n)
        if(m=='polarity_confidence'):
            pol.append(n)
        if(m=='subjectivity_confidence'):
            sub.append(n)

print(pol)
print(sub)
counts = Counter(ll)
print(counts)

labels, values = zip(*counts.items())
indSort = np.argsort(values)[::-1]

labels = np.array(labels)[indSort]
values = np.array(values)[indSort]
indexes = np.arange(len(labels))
bar_width = 0.10
plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()



plt.hist(pol, density=True, bins=le)
plt.ylabel('Probability');
