import pymysql
from connections.connection import Connection

class MySQLConnection(Connection):
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(
            host=host, 
            user=user, 
            password=password, 
            database=database)
        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor
    
    def execute(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)

    def commit(self):
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def get_last_row_id(self):
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.connection.close()