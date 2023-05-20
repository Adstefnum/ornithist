import time
from bs4 import BeautifulSoup
import lxml
import requests

bird_names=[]
DESC_XPATH="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]"
IMAGE_XPATH="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[2]/td/a/img"
WIKI_URL= "https://en.wikipedia.org/wiki/"
result = []

def get_page(name):
    link = WIKI_URL+name
    page = requests.get()
    return page,link

def get_desc(page):
    pass

def get_img(page):
    pass

#save to json or csv and upload to appwrite and make a function API to query the db
#or write directly to appwrite database
for name in bird_names:
    page,link = get_page(name)
    desc = get_desc(page)
    img = get_img(page)
    result.append([name,desc,img,link])
    time.sleep(1)


#https://www.geeksforgeeks.org/web-scraping-from-wikipedia-using-python-a-complete-guide/
