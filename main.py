from credentials import *
from connections.sqlconnection import MySQLConnection
from connections.mongoconnection import MongoConnection

#conexion a MongoDB
mongo = MongoConnection(MONGO_URI, MONGO_DB)
db = mongo.get_db()

#conexion a MySQL
mysql = MySQLConnection(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
cursor = mysql.get_cursor()

print("Conexiones establecidas")
print(" - MongoDB -> coleccion.find({...})")
print(" - MySQL   -> cursor.execute(...) y cursor.fetchall()")