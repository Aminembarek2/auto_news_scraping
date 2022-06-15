from turtle import title
import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import json


def grab_data(url):
    try:
        page=requests.get(url) 
    except Exception as e:    
        error_type, error_obj, error_info = sys.exc_info()      
        print ('ERROR FOR LINK:',url)
        print (error_type, 'Line:', error_info.tb_lineno)
        exit()
    html = page.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

url = 'https://globalnews.ca/world/'
soup = grab_data(url)
main = soup.findAll(attrs={'class':'l-section__main'})
titles = []

for i in range(len(main)):
    titles = titles[:len(titles)-2] + main[i].findAll(attrs={'class':'c-posts__inner'})

for i in titles:
    for j in i.findAll('div',attrs={'class':'c-posts__about'}):
        j.replace_with('')


data_list=[]
dic = {}

# get titles and links as description

for i in range(len(titles)):
    images = titles[i].find('img',attrs={'class':'c-posts__thumbnail'})
    title = titles[i].find('span',attrs={'class':'c-posts__headlineText'})
    if images!=[] and images!=None:
        image = images.get('data-src')
        if image==None:
            image = images.get('src')
    if titles[i].get("href") != None:
        dic = {
            'title':title.text,
            'description':titles[i].get("href"),
            'image':image,
            'time':None
        }
        data_list.append(dic)

for i in data_list:
    soup=grab_data(i['description'])
    body = soup.findAll('div',attrs={'class':'l-main__article'})
    for j in body[0].findAll('p',attrs={'class':'c-readmore'}):
        j.replace_with('')
    body[0].text.replace('read me','')
    body[0].text.replace('read more','')
    body[0].text.replace('\n','')
    description_text=[]
    for j in range(len(body)):
        description_text += body[j].findAll('p')
    description=""

    times = soup.find('div',attrs={'class':'c-byline__date'}).text
    times = times.split()
    time = ""

    for j in range(1,4):
        time += times[j] + " "
    if description_text!= None and description_text!=[]:
        for j in description_text:
            description += j.text


    i['description']=description
    i['time']=time

data = json.dumps(data_list)
f = open("data/world_news/raw_data.json", "r+")
f.truncate(0)
f.write(data)
f.close()