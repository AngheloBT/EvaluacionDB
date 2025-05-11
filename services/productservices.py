from repositories.productrepository import ProductRepository
from models.product import Product
from typing import List, Optional

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_product(self, product: Product) -> Product:
        self._verificar_no_existencia(product.get_sku())
        return self.product_repository.add_product(product)

    def get_product_by_sku(self, sku: str) -> Optional[Product]:
        return self.product_repository.get_product_by_sku(sku)

    def update_product(self, product: Product) -> None:
        self._verificar_existencia(product.get_sku())
        self.product_repository.update_product(product)

    def delete_product(self, sku: str) -> None:
        self._verificar_existencia(sku)
        self.product_repository.delete_product(sku)

    def get_all_products(self) -> List[Product]:
        return self.product_repository.show_all_products()

    def _verificar_existencia(self, sku: str) -> None:
        if not self.product_repository.get_product_by_sku(sku):
            raise ValueError(f"Producto con SKU {sku} no existe.")

    def _verificar_no_existencia(self, sku: str) -> None:
        if self.product_repository.get_product_by_sku(sku):
            raise ValueError(f"Producto con SKU {sku} ya existe.")
