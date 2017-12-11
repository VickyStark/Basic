import urllib.request
import random

def image_download(url):
    name=random.randrange(1,100)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)

image_download("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYmowOJ3aqe6G0s0TLJPC7tlNc51en9e4QxE_oFzkMEwpxxJ8T")