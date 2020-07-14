from pymongo import MongoClient
import json
import pandas as pd


conn = MongoClient(host='localhost', port=27017)
db = conn.test_db
project = db.project
tasks = db.tasks

my_csv = pd.read_csv("./csv_2.csv")
my_json = my_csv.to_json('data.json')

with open ("./data.json") as f:
    data = json.load(f)
    project.insert_one(data)
    for row in project.find({"status":"canceled"}):
        print(row)

#Here will be function to convert csv to json
