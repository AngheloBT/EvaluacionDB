import pymysql

class MySQLConnection:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def get_cursor(self):
        return self.cursor
    
    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()