from http import client
import pandas as pd  
import petl as etl
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/',username="rootuser", password="rootpass")

db = client['mydb']
data = pd.read_csv('formated_csv.csv')
data=data.to_dict(orient="records")
db.mycollection.insert_many(data)
print(data)