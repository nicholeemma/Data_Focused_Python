# coding:utf-8 
import requests 
from lxml import html
import pandas as pd
fout = open('datafromrs.txt', 'wt', encoding='utf-8')
name=['']*600
price=['']*600
address=['']*600
stars=['']*600

a=0
for j in range(0,600,30):
    url ='https://www.yelp.com/search?find_desc=Restaurants&find_loc=Adelaide,+Adelaide+South+Australia,+Australia&start='+(str)(j)
    con = requests.get(url).content 
    sel = html.fromstring(con) 
    

    for i in sel.xpath('//li[@class="regular-search-result"]'):
        name[a]=i.xpath('div/div/div/div[2]/div[1]/div[1]/h3/span/a/span/text()')
        
       
        price[a]=i.xpath('div/div/div/div[2]/div[1]/div[1]/div[2]/span[1]/span/text()')
##        print(price)
        address[a]=i.xpath('div/div/div/div[2]/div[1]/div[2]/address/text()'.strip())
        
##        print(address)
        stars[a]=i.xpath('div/div/div/div[2]/div[1]/div[1]/div[1]/div/@title')
        a+=1
##        b+=1
print(len(name))
data={'name':name,'address':address,'stars':stars}
frame=pd.DataFrame(data)
frame.to_csv('Reatarant_Information1.csv', sep=',', header=True, index=True)

##for x in name:
##    fout.writelines()
##print(name)
##print(address)
##print(stars)
