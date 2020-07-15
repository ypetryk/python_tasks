from pymongo import MongoClient
import json
import pandas as pd

# creating database and two collections('project','tasks')
conn = MongoClient(host='localhost', port=27017)
db = conn.test_db
project = db.project
tasks = db.tasks

# importing data from csv to json
pd.read_csv("./csv_1.csv").to_json('project.json', orient = 'records', indent = 4)
pd.read_csv("./csv_2.csv").to_json('tasks.json', orient = 'records', indent = 4)

# writing data from json file to collection 'tasks'
with open('./tasks.json') as f:
    data = json.load(f)
    for el in data:
        tasks.insert_one(el)

# fetching 'project name' for 'status = canceled'
for row in tasks.find({"status":"canceled"}):
        print(row['project'])
