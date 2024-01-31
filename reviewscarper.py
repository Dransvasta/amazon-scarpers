import requests
from bs4 import BeautifulSoup
import pandas as pd
'''
html = requests.get('https://www.amazon.com/Xbox-Starter-hundreds-Ultimate-Membership-All-Digital/product-reviews/B0CFS1SDC4/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',headers={
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
    })
bs4page  = BeautifulSoup(html.text,'html.parser')


reviewdiv = bs4page.find(id='cm_cr-review_list')
reviewslist = reviewdiv.find_all('div',class_='a-section review aok-relative')'''
dlist=[]
pagenum=1
while(1):
    html = requests.get('https://www.amazon.com/Xbox-Starter-hundreds-Ultimate-Membership-All-Digital/product-reviews/B0CFS1SDC4/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(pagenum),headers={
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
    })
    if html.status_code!=200:
       break
    bs4page  = BeautifulSoup(html.text,'html.parser')
    reviewdiv = bs4page.find(id='cm_cr-review_list')
    reviewslist = reviewdiv.find_all('div',class_='a-section review aok-relative')
    if len(reviewslist)==0:
       break
    print("pagenum:"+str(pagenum))
    co=0
    for i in reviewslist:
      #print(co)
      d={}
      d['name']=i.find('div',class_='a-profile-content').text
      titlea=i.find('a',attrs={'data-hook':'review-title'})
      if titlea:
        pass
      else:
        titlea=i.find_all('div',class_="a-row a-spacing-none")[1]
      titlespanlist = titlea.find_all('span')
      title = titlespanlist[2].text
      ratting = titlespanlist[0].text.split()[0]
      d['title']=title
      d['ratting']=ratting
      reviewbody = i.find('span',attrs={'data-hook':'review-body'})
      d['review']=reviewbody.text
      co+=1
      dlist.append(d)
    pagenum+=1
df= pd.DataFrame(dlist)
df.to_excel('output/reviews.xlsx')
#fi = open('reviewpage.html','w',encoding='utf-8')
