import requests
from bs4  import BeautifulSoup
import pandas as pd
search="Xbox One"
page=1
headers1 = {
      'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
dlist=[]
limit=20
while(1):
    if page>limit:
        break
    html = requests.get("https://www.amazon.com/s?k="+str(search)+"%page="+str(page),headers=headers1)
    if html.status_code!=200:
        break
    apagebs4 = BeautifulSoup(html.text,'html.parser')
    #print(apagebs4.prettify())
    span1 = apagebs4.body.find_all('span',class_='rush-component s-latency-cf-section')[0]
    divrows = span1.find_all('div',class_='s-main-slot s-result-list s-search-results sg-row')[0]
    #divs = apagebs4.body.find_all('div',class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')[0]
    results1 = divrows.find_all("div",{"data-component-type": "s-search-result"})
    results2 = divrows.find_all("div",class_="AdHolder",attrs={"data-component-type":"s-search-result"})
    results=[]
    fi = open('bs43.txt','w')
    print("pagenum:"+str(page))
    for i in results1:
        if i not in results2:
            resincol= i.find_all(class_="puisg-col-inner")
            results.append(resincol[:3])
    print(len(results))
    for i in results:
        d=dict()
        image=i[0].find_all('img',class_='s-image')
        header=i[1].find('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        price = i[2].find('span',class_="a-offscreen")
        d['title']=header.text
        d['product-url']=header['href']
        d['image-src']=image[0]['src']
        if price!=None:
            d['price']=price.text
        dlist.append(d)
    page+=1
df = pd.DataFrame(dlist)
df.to_excel('output/serchresults.xlsx',index=False)