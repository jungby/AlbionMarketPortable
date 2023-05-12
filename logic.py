from tab_precios import Ui_Dialog as tb_p
import requests
from pymongo import MongoClient
from decouple import config

BASE_URL = 'https://www.albion-online-data.com/api/v2/stats/Prices/'

# Conectar a la base de datos
client = config("MONGOAPI")
client = MongoClient(client)
db = client['AlbionMarketplace']

items = db['items']
world = db['world']

city_names = []
for city_doc in world.find():
    city_name = city_doc['UniqueName']
    city_names.append(city_name)

item_names = []
for item_doc in items.find():
    item_name = item_doc['UniqueName']
    item_names.append(item_name)

unique_tags = items.distinct("tags")

item_names.sort()
city_names.sort()