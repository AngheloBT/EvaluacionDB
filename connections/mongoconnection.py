from pymongo import MongoClient

class MongoConnection:
    def __init__(self, uri: str, dbname: str):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        
    def get_db(self):
        return self.db
    
    def close(self):
        self.client.close()