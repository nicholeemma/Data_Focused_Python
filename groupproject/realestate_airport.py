# coding:utf-8 
import requests 
from lxml import html
import pandas as pd
##fout = open('datafromrs.txt', 'wt', encoding='utf-8')
price=[]
location=[]
bed=[]
#scarp 100 houses information
#each page will present 20 houses, so only scarp 5 pages
bath=['a']*100
car=['0']*100
detailurl=['']*100
f=0
for j in range(5):
    url ='https://www.realestate.com.au/rent/in-adelaide+airport,+sa+5950/list-'+(str)(j)
   
    con = requests.get(url).content 
    sel = html.fromstring(con) 
    

    for i in sel.xpath('//div[@class="listingInfo rui-clearfix"]'):
        price.extend(i.xpath('div[@class="propertyStats"]/p/text()'.strip()))
        #print(price)
        location.extend(i.xpath('div[@class="vcard"]/h2/a[@class="name"]/text()'))
        #print(location)
        bed.extend(i.xpath('dl[@class="rui-property-features rui-clearfix"]/dd[1]/text()'))
##        bath.extend(i.xpath('dl[@class="rui-property-features rui-clearfix"]/dd[2]/text()'))
        bath[f]=i.xpath('dl[@class="rui-property-features rui-clearfix"]/dd[3]/text()')
        car[f]=i.xpath('dl[@class="rui-property-features rui-clearfix"]/dd[3]/text()')
        
        href=i.xpath('div[@class="vcard"]/h2/a[@class="name"]/@href')[0].strip()
        hreff=f'https://www.realestate.com.au{href}'
        detailurl[f]=hreff
        f+=1
       # print(detailurl)
#print(type(sel.xpath('//div[@class="listingInfo rui-clearfix"]')))
#print(len(price),len(location),len(bed),len(bath),len(car),len(detailurl))
##print(car)
#store data into dataframe
data={'price':price,'location':location,'bed':bed,'bath':bath,'car':car,'url':detailurl}
fram=pd.DataFrame(data)
#print(fram)
#store data into csv file
fram.to_csv('house_Information_Airport.csv', sep=',', header=True, index=True)

