from bs4  import BeautifulSoup
from seleniumbase import Driver
#import pandas as pd
import json 
d=dict()
driver = Driver(uc=True,headless=True)
driver.get("https://www.amazon.com/Xbox-Starter-hundreds-Ultimate-Membership-All-Digital/dp/B0CFS1SDC4")
html= driver.page_source
driver.close()
bs4 = BeautifulSoup(html,'html.parser')
corepricediv = bs4.find('div',id='corePriceDisplay_desktop_feature_div')
titlediv = bs4.find(id="productTitle")

price = corepricediv.find(class_='a-offscreen').text
aboutthisdiv = bs4.find('div',id='feature-bullets')
about_this = aboutthisdiv.find('ul',class_='a-unordered-list a-vertical a-spacing-mini')
about=""
product_detailsdiv = bs4.find('div',id="prodDetails")
#fi = open('producttables.txt','w')
reviewdiv = bs4.find('div',id="reviews-medley-footer")
reviewlink = reviewdiv.find('a',attrs={'data-hook':'see-all-reviews-link-foot'})
dpro={}
for i in product_detailsdiv.find_all('table'):
    if i.tbody:
        for j in i.tbody.find_all('tr'):
            if j.th.text.strip() == "Customer Reviews":
                listd=j.td.text.split()
                dpro[j.th.text]= listd[0]+str(", ")+listd[6]+" "+listd[7]
            else:
                dpro[j.th.text]=j.td.text
    else:
        #fi.write(str(i)+'\n')
        pass 

for i in about_this.find_all('li',class_='a-spacing-mini'):
    about+=i.text+"\n"
d['title']=titlediv.text.strip()
d['price']=price
d['About this item']=about
d['product-information']=dpro
d['reviewlink']=reviewlink['href']

with open("output/product.json", "w") as f:
    json.dump(d, f)