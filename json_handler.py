import json 
import os.path
import os
import stat
import datetime

if not os.path.isfile('./data.json'):
    with open('data.json', 'w') as json_file:
        json.dump({"Default Item": 5}, json_file)

if not os.path.isfile('./sales_data.json'):
    with open('sales_data.json', 'w') as json_file:
        json.dump({"Default Item": {"profit": 1, "sales":{datetime.datetime.now().strftime("%Y"): {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "Jun": 0 , "Jul": 0, "Aug":0, "Sep": 0, "Oct": 0, "Nov":0, "Dec":0}}}}, json_file)

os.chmod('./data.json', stat.S_IRWXU | stat.S_IRWXO)
os.chmod('./sales_data.json', stat.S_IRWXU | stat.S_IRWXO)

def load_data():
    with open('./data.json') as json_file:
        data = json.load(json_file)
        return data

def change_data(data):
    with open('./data.json', 'w') as json_file:
        json.dump(data, json_file)

def load_sales_data():
    with open('./sales_data.json') as json_file:
        data = json.load(json_file)
        flag = False
        for key in data.keys():
            if datetime.datetime.now().strftime("%Y") not in data[key]["sales"]:
                data[key]["sales"][datetime.datetime.now().strftime("%Y")] = {"Jan":0,"Feb":0,"Mar":0,"Apr":0,"May":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Oct":0,"Nov":0,"Dec":0}
                flag = True
        if flag:
            change_sales_data(data)
        return data

def change_sales_data(data):
    with open('./sales_data.json', 'w') as json_file:
        json.dump(data, json_file)