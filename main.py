from credentials import *
from connections import mongoconnection
from connections import mysqlconnection

#conexion a MongoDB
mongo = mongoconnection.MongoConnection(MONGO_URI, MONGO_DB)
db = mongo.get_db()

#conexion a MySQL
mysql = mysqlconnection.MySQLConnection(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
cursor = mysql.get_cursor()

print("Conexiones establecidas")