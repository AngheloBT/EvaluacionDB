from connections.sqlconnection import MySQLConnection
from connections.mongoconnection import MongoConnection
from repositories.clientrepository import ClientRepository
from repositories.productrepository import ProductRepository
from repositories.orderrepository import OrderRepository
from services.clientservices import ClientService
from services.productservices import ProductService
from services.orderservices import OrderService
from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()

        self.mysql_connection = MySQLConnection(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )

        self.mongo_connection = MongoConnection(
            uri=os.getenv("MONGO_URI"),
            dbname=os.getenv("MONGO_DB")
        )
        # Repositorios
        self.client_repository = ClientRepository(connection=self.mysql_connection)
        self.product_repository = ProductRepository(connection=self.mongo_connection)
        self.order_repository = OrderRepository(connection=self.mongo_connection)

        # Servicios
        self.client_service = ClientService(client_repository=self.client_repository)
        self.product_service = ProductService(product_repository=self.product_repository)
        self.order_service = OrderService(
            order_repo=self.order_repository,
            product_repo=self.product_repository,
            client_repo=self.client_repository
        )
