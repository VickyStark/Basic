import requests
from bs4 import BeautifulSoup
import html

def crawler(max_pages):
    pages=1
    while pages <= max_pages:
        url = "https://www.flipkart.com/search?q=smart%20phones&as=on&as-show=on&otracker=start&as-pos="+str(pages)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,"html.parser")
        for link in soup.find_all('a',{'class':'title'}):
            title=link.string
            connect=link.get('href')
            print(title)
            print(connect)
            pages +=1

crawler(1)