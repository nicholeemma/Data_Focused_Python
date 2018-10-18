from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

import pandas as pd

name=[]
address=[]
rate=[]

for j in range(3):
    html = urlopen('https://www.yelp.com/search?find_desc=Restaurants&find_loc=Adelaide,+Adelaide+South+Australia,+Australia&start='+(str)(j))
    bsyc = BeautifulSoup(html.read(), "lxml")
    address.extend(bsyc.findAll('address')[0].contents)
    tc_name = bsyc.findAll('a', { "class" : "biz-name js-analytics-click" })[0]
    for r in tc_name.children:
        name.extend(r.contents)
    tc_rate=bsyc.findAll('div',{ "class" : "biz-rating biz-rating-large clearfix" })[0]
    u=0
    for x in tc_rate.children:
        u=u+1
        if(u==2):
            rates=(x['title'])
            rate.append(rates)


print(rate)
print(name)
print(address)
np_name=np.array(name)
np_address=np.array(address)
np_rate=np.array(rate)
data={'name':np_name,'address':np_address,'rate':np_rate}
