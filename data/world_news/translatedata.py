from googletrans import Translator
import json
import data.world_news.getdata

translator = Translator()
r = open("data/world_news/raw_data.json", "r")
w = open("data/world_news/data.json", "r+")
file = json.loads(r.read())
data_list = []
data ={} 
for i in file:
    if i['title'] != None and i['description'] != None and i['time']!= None:
        head = translator.translate(i['title'], src='en',dest='ar')
        description = translator.translate(i['description'], src='en',dest='ar')
        time = translator.translate(i['time'], src='en',dest='ar')
        time = u"\u202B {}".format(time.text)
        title = u"\u202B {}".format(head.text) 
        description = u"\u202B {}".format(description.text)
        data = {
            'title':title,
            'description':description,
            'image':i['image'],
            'time':time,
        }
        data_list.append(data)
data_json = json.dumps(data_list)
w.truncate(0)
w.write(data_json)
w.close()
r.close()