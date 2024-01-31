from seleniumbase import Driver
from bs4  import BeautifulSoup
driver = Driver(uc=True)
driver.get("https://www.amazon.com/Outriders-Xbox-One-Standard/dp/B07SH3DJL9")
html= driver.page_source
driver.close()
bs4 = BeautifulSoup(html,'html.parser')

fi = open('bs34.html','w',encoding='utf-8')
fi.write(str(bs4.prettify()))