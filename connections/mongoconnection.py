from pymongo import MongoClient

class MongoConnection:
    def __init__(self, uri: str, dbname: str):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        
    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("✅ Conexión a MongoDB exitosa.")
        except Exception as e:
            print(f"❌ Error al conectar a MongoDB: {e}")

    def get_database_name(self):
        """Devuelve el nombre de la base de datos actual."""
        return self.db.name
        
    def get_db(self):
        return self.db
    
    def get_collection(self, collection_name: str):
        return self.db[collection_name]
    
    def close(self):
        self.client.close()