import os


AWS_S2_BUCKET_NAME = 'wafer-fault'
MONGO_DATABASE_NAME = 'Vijay_vsnv'
MONGO_COLLECTION_NAME  = 'waferfault'

TARGET_COLUMN = 'quality'
username = "vijayvsnv"
password = "Avanti@906"
MONGO_DB_URL = f"mongodb+srv://{username}:{password}@cluster0.foekzrg.mongodb.net/?retryWrites=true&w=majority"
MODEL_FULL_NAME = 'model'
MODEL_FILE_EXTENSION = '.pkl'

artifact_folder = 'artifacts'