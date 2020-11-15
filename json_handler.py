import json 

def load_data():
    with open('./data.json') as json_file:
        data = json.load(json_file)
        return data

def change_data(data):
    with open('./data.json', 'w') as json_file:
        json.dump(data, json_file)
