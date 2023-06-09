import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()

# "mongodb url mongodb+srv://shivanshjayara2991:u1CBs4bWlnVB8TIP@cluster0.twv9vbd.mongodb.net/?retryWrites=true&w=majority"

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                # mongo_db_url = "mongodb+srv://shivanshjayara2991:shivansh180cc@cluster0.twv9vbd.mongodb.net/?retryWrites=true&w=majority"
                # if "localhost" in mongo_db_url:
                #     MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                # else:
                MongoDBClient.client = pymongo.MongoClient(os.environ, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e


# mongodb+srv://shivanshjayara2991:shivansh180cc@cluster0.twv9vbd.mongodb.net/?retryWrites=true&w=majority