from pymongo.mongo_client import MongoClient
import pandas as pd 
import json

from pymongo import MongoClient
from urllib.parse import quote_plus

username = quote_plus("vijayvsnv")
password = quote_plus("Avanti@906")  # This will become 'Avanti%40906'

uri = f"mongodb+srv://{username}:{password}@cluster0.foekzrg.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)



# create database ame andV collection
DATABASE_NAME="Vijay_vsnv"
COLLECTION_NAME="waferfault"

 
df = pd.read_csv("C:\Users\HP\Desktop\sensorproject\notebooks\wafer.csv")

df.head()
df = df.drop("wafer",axis=1)


json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

