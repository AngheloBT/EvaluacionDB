from repositories.orderrepository import OrderRepository
from repositories.productrepository import ProductRepository
from repositories.clientrepository import ClientRepository
from models.orders import Pedido as Order 
from models.product import Product
from models.client import Client
from typing import List

class OrderService:
    def __init__(self, order_repo: OrderRepository, product_repo: ProductRepository, client_repo: ClientRepository):
        self.order_repo = order_repo
        self.product_repo = product_repo
        self.client_repo = client_repo

    def add_order(self, order: Order) -> Order:
        client = self._obtener_cliente(order.get_cliente_rut())

        total = 0.0
        productos_actualizados = []

        for item in order.get_productos():
            sku = item["sku"]
            cantidad = item["cantidad"]

            producto = self._obtener_producto(sku)

            if cantidad > producto.get_stock():
                raise ValueError(f"Stock insuficiente para producto {sku} (Disponible: {producto.get_stock()}, Solicitado: {cantidad})")
            total += cantidad * producto.get_precio()
            producto.set_stock(producto.get_stock() - cantidad)
            productos_actualizados.append(producto)

        for producto in productos_actualizados:
            self.product_repo.update_product(producto)

        order.set_total(total)

        return self.order_repo.add_order(order)

    def get_all_orders(self) -> List[Order]:
        return self.order_repo.show_all_orders()

    def get_orders_by_rut(self, rut: str) -> List[Order]:
        return self.order_repo.get_orders_by_rut(rut)

    def _obtener_cliente(self, rut: str) -> Client:
        client = self.client_repo.get_client_by_rut(rut)
        if not client:
            raise ValueError(f"Cliente con RUT {rut} no encontrado.")
        return client

    def _obtener_producto(self, sku: str) -> Product:
        product = self.product_repo.get_product_by_sku(sku)
        if not product:
            raise ValueError(f"Producto con SKU {sku} no encontrado.")
        return product
