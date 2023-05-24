import requests
from pymongo import MongoClient
from decouple import config

# Define the base URL for the Albion Online Data API
BASE_URL = 'https://www.albion-online-data.com/api/v2/stats/Prices/'

# Connect to the MongoDB database using the credentials in the .env file
client = MongoClient(config("MONGOAPI"))
db = client['AlbionMarketplace']

items = db['items']
world = db['locations']

# Get a list of all city names from the "locations" collection
city_names = []
for city_doc in db.locations.find():
    city_name = city_doc['UniqueName']
    city_names.append(city_name)

# Get a list of all item names from the "items" collection
item_names = []
for item_doc in db.items.find():
    item_name = item_doc['UniqueName']
    item_names.append(item_name)

# Create a dictionary of item details, using the item's unique name as the key
item_sp_dict = {}
for item_sp_doc in db.items.find():
    item_unique_name = item_sp_doc['UniqueName']
    item_name = item_sp_doc['Name']
    item_description = item_sp_doc['Description']
    item_image = item_sp_doc['ImageURL']
    item_tag = item_sp_doc['tags'][0]

    item_sp_dict[item_unique_name] = {
        'name': item_name,
        'description': item_description,
        'image': item_image,
        'tag': item_tag
    }

# Create a dictionary of city details, using the city's name as the key
city_sp_dict = {}
for city_sp_doc in db.locations.find():
    city_unique_name = city_sp_doc['UniqueName']
    city_description = city_sp_doc['Description']

    city_sp_dict[city_unique_name] = {
        'description': city_description
    }

unique_tags = items.distinct("tags")
unique_tags.append('Any')
unique_tags.sort()

item_names.sort()
city_names.sort()