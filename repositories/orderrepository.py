# repositories/order_repository.py
from models.orders import Pedido as Order
from connections.mongoconnection import MongoConnection
from pymongo.collection import Collection
from typing import List

class OrderRepository:
    def __init__(self, connection: MongoConnection):
        self.collection: Collection = connection.get_collection("pedidos")

    def add_order(self, order: Order) -> Order:
        self.collection.insert_one(order.to_dict())
        return order

    def get_orders_by_rut(self, rut: str) -> List[Order]:
        results = self.collection.find({"cliente_rut": rut})
        orders = []
        for doc in results:
            order = Order()
            order.from_dict(doc)
            orders.append(order)
        return orders

    def show_all_orders(self) -> List[Order]:
        orders = []
        for doc in self.collection.find():
            order = Order()
            order.from_dict(doc)
            orders.append(order)
        return orders
    

    def get_all_orders(self):
        """Obtiene todos los pedidos desde la colección de MongoDB."""
        return list(self.collection.find())

    def get_orders_by_rut(self, rut):
        """Obtiene los pedidos de un cliente por su RUT."""
        return list(self.collection.find({"cliente_rut": rut}))
