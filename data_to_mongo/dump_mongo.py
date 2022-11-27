import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os
from dotenv import load_dotenv
load_dotenv()

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient(os.getenv("MONGODB_CREDENTIALS"))

@dataclass
class EnvironmentVariable(object):
    DATA_FILE_PATH:str=os.getenv("DATA_FILE_PATH")
    DATABASE_NAME:str=os.getenv("DATABASE_NAME")
    COLLECTION_NAME:str=os.getenv("COLLECTION_NAME")


env=EnvironmentVariable()
if __name__=="__main__":
    df = pd.read_csv(env.DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongo db
    client[env.DATABASE_NAME][env.COLLECTION_NAME].insert_many(json_record)
