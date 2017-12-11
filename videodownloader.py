import urllib.request
import random

def image_download(url):
    name=random.randrange(1,100)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)

image_download(#Paste Your URL)