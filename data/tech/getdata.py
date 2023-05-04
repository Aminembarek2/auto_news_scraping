import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import json


def grab_data(url):
    url = 'https://www.reuters.com'+url
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

url = '/technology'
soup = grab_data(url)
main = soup.findAll(attrs={'id':'main-content'})

titles = main[0].findAll('a',attrs={'data-testid':'Heading'})
for i in titles:
    for j in i.findAll('span',attrs={'data-testid':'VisuallyHidden'}):
        j.replace_with('')

data_list=[]
dic = {}

# get titles and links as description
for i in range(len(titles)):
    dic = {
        'title':titles[i].text,
        'description':titles[i].get("href"),
    }
    if dic['description'][:3]=='htt':
        del(dic[titles[i].get("href")])

    data_list.append(dic)

no_news = []
for i in data_list:
    soup=grab_data(i['description'])
    body = soup.findAll('div',attrs={'class':'article-body__content__17Yit'})
    images = soup.findAll('div',attrs={'data-testid':'primary-image'})
    description = ""
    image = None

    #remove pub and read me links
    for j in body[0].findAll('div',attrs={'class':'registration-prompt__container__2jf5K'}):
        j.replace_with('')
    for j in body[0].findAll('p',attrs={'data-testid':'Body'}):
        j.replace_with('')
    body[0].text.replace('read me','')
    body[0].text.replace('read more','')

    time = soup.find('span',attrs={'class':'date-line__date__23Ge-'}).text

    if body!=None and body!=[]:
        for j in body:
            description += j.text

        if images!=[] and images!=None:
            #Scrap Image
            string = images[0].find('noscript')
            image = BeautifulSoup(str(string), "html.parser")
            if image.find('img') is not None:
                image = image.find('img').get('src')
            else:
                image = None
    else:
        no_news.append(i)

    i['description']=description
    i['image']=image
    i['time']=time

for i in data_list:
    if i in no_news:
        data_list.remove(i)

data = json.dumps(data_list)
f = open("data/tech/raw_data.json", "r+")
f.truncate(0)
f.write(data)
f.close()