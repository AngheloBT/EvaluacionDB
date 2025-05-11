# repositories/product_repository.py
from models.product import Product
from connections.mongoconnection import MongoConnection
from pymongo.collection import Collection
from typing import Optional, List

class ProductRepository:
    def __init__(self, connection: MongoConnection):
        self.collection: Collection = connection.get_collection("productos")

    def add_product(self, product: Product) -> Product:
        self.collection.insert_one(product.to_dict())
        return product

    def get_product_by_sku(self, sku: str) -> Optional[Product]:
        result = self.collection.find_one({"sku": sku})
        if result:
            product = Product()
            product.from_dict(result)
            return product
        return None

    def update_product(self, product: Product) -> bool:
        result = self.collection.update_one(
            {"sku": product.get_sku()},
            {"$set": product.to_dict()}
        )
        return result.matched_count > 0

    def delete_product(self, sku: str) -> bool:
        result = self.collection.delete_one({"sku": sku})
        return result.deleted_count > 0

    def show_all_products(self) -> List[Product]:
        productos = []
        for doc in self.collection.find():
            product = Product()
            product.from_dict(doc)
            productos.append(product)
        return productos
