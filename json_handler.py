import json 
import os.path
import os
import stat

if not os.path.isfile('./data.json'):
    with open('data.json', 'w') as json_file:
        json.dump({"Default Item": 5}, json_file)

os.chmod('./data.json', stat.S_IRWXU | stat.S_IRWXO)

def load_data():
    with open('./data.json') as json_file:
        data = json.load(json_file)
        return data

def change_data(data):
    with open('./data.json', 'w') as json_file:
        json.dump(data, json_file)
