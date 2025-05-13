from credentials import *
from connections.sqlconnection import MySQLConnection
from connections.mongoconnection import MongoConnection
from models.client import Client
from models.product import Product
from models.orders import Pedido
from repositories.clientrepository import ClientRepository
from repositories.productrepository import ProductRepository
from repositories.orderrepository import OrderRepository
from services.productservices import ProductService
from services.clientservices import ClientService
from services.orderservices import OrderService
from datetime import datetime, timezone

# Conexión a MongoDB
mongo = MongoConnection(MONGO_URI, MONGO_DB)
db = mongo.get_db()

# Conexión a MySQL
mysql = MySQLConnection(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
cursor = mysql.get_cursor()

# Seleccionar la base de datos
cursor.execute(f"USE {MYSQL_DB};")
print(f"Base de datos '{MYSQL_DB}' seleccionada.")

print("Conexiones establecidas")
print(" - MongoDB -> coleccion.find({...})")
print(" - MySQL   -> cursor.execute(...) y cursor.fetchall()")

def mostrar_tabla(datos: list, encabezados: list):
    # Calcular el ancho máximo de cada columna
    anchos = [len(encabezado) for encabezado in encabezados]
    for fila in datos:
        for i, valor in enumerate(fila):
            anchos[i] = max(anchos[i], len(str(valor)))

    # Crear la línea separadora
    separador = "+".join("-" * (ancho + 2) for ancho in anchos)
    separador = f"+{separador}+"

    # Imprimir encabezados
    print(separador)
    encabezado_formateado = "| " + " | ".join(encabezado.ljust(anchos[i]) for i, encabezado in enumerate(encabezados)) + " |"
    print(encabezado_formateado)
    print(separador)

    # Imprimir filas
    for fila in datos:
        fila_formateada = "| " + " | ".join(str(valor).ljust(anchos[i]) for i, valor in enumerate(fila)) + " |"
        print(fila_formateada)
    print(separador)

# Repositorios
client_repo = ClientRepository(mysql)
product_repo = ProductRepository(mongo)
order_repo = OrderRepository(mongo)

# Servicios
client_service = ClientService(client_repo)
product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo, client_repo)

def menu_clientes():
    while True:
        print("\n--- Menú Clientes ---")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Buscar cliente por RUT")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                cliente = Client()
                cliente.set_rut(input("Ingrese el RUT del cliente: "))
                cliente.set_name(input("Ingrese el nombre del cliente: "))
                cliente.set_email(input("Ingrese el email del cliente: "))
                cliente.set_phone(int(input("Ingrese el teléfono del cliente: ")))
                cliente.set_address(input("Ingrese la dirección del cliente: "))
                client_service.add_client(cliente)
                print("Cliente creado exitosamente.")
            elif opcion == "2":
                clientes = client_service.get_all_clients()
                datos = [[cliente.get_rut(), cliente.get_name(), cliente.get_email(), cliente.get_phone(), cliente.get_address()] for cliente in clientes]
                encabezados = ["RUT", "Nombre", "Email", "Teléfono", "Dirección"]
                mostrar_tabla(datos, encabezados)
            elif opcion == "3":
                rut = input("Ingrese el RUT del cliente: ")
                cliente = client_service.get_client_by_rut(rut)
                if cliente:
                    datos = [[cliente.get_rut(), cliente.get_name(), cliente.get_email(), cliente.get_phone(), cliente.get_address()]]
                    encabezados = ["RUT", "Nombre", "Email", "Teléfono", "Dirección"]
                    mostrar_tabla(datos, encabezados)
                else:
                    print("Cliente no encontrado.")
            elif opcion == "4":
                rut = input("Ingrese el RUT del cliente a actualizar: ")
                cliente = client_service.get_client_by_rut(rut)
                if not cliente:
                    print(f"Cliente con RUT {rut} no encontrado.")
                    continue
                print("Deje en blanco los campos que no desea actualizar.")
                nombre = input(f"Nombre actual ({cliente.get_name()}): ") or cliente.get_name()
                email = input(f"Email actual ({cliente.get_email()}): ") or cliente.get_email()
                telefono = input(f"Teléfono actual ({cliente.get_phone()}): ") or cliente.get_phone()
                direccion = input(f"Dirección actual ({cliente.get_address()}): ") or cliente.get_address()
                cliente.set_name(nombre)
                cliente.set_email(email)
                cliente.set_phone(telefono)
                cliente.set_address(direccion)
                client_service.update_client(cliente)
                print("Cliente actualizado exitosamente.")
            elif opcion == "5":
                rut = input("Ingrese el RUT del cliente a eliminar: ")
                client_service.delete_client(rut)
                print("Cliente eliminado exitosamente.")
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except Exception as e:
            print(f"Error: {e}")

def menu_productos():
    while True:
        print("\n--- Menú Productos ---")
        print("1. Crear producto")
        print("2. Ver productos")
        print("3. Buscar producto por SKU")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                producto = Product()
                producto.set_sku(input("Ingrese el SKU del producto: "))
                producto.set_marca(input("Ingrese la marca del producto: "))
                producto.set_modelo(input("Ingrese el modelo del producto: "))
                producto.set_precio(float(input("Ingrese el precio del producto: ")))
                producto.set_stock(int(input("Ingrese el stock del producto: ")))
                product_service.add_product(producto)
                print("Producto creado exitosamente.")
            elif opcion == "2":
                productos = product_service.get_all_products()
                datos = [[producto.get_sku(), producto.get_marca(), producto.get_modelo(), producto.get_precio(), producto.get_stock()] for producto in productos]
                encabezados = ["SKU", "Marca", "Modelo", "Precio", "Stock"]
                mostrar_tabla(datos, encabezados)
            elif opcion == "3":
                sku = input("Ingrese el SKU del producto: ")
                producto = product_service.get_product_by_sku(sku)
                if producto:
                    datos = [[producto.get_sku(), producto.get_marca(), producto.get_modelo(), producto.get_precio(), producto.get_stock()]]
                    encabezados = ["SKU", "Marca", "Modelo", "Precio", "Stock"]
                    mostrar_tabla(datos, encabezados)
                else:
                    print("Producto no encontrado.")
            elif opcion == "4":
                sku = input("Ingrese el SKU del producto a actualizar: ")
                producto = product_service.get_product_by_sku(sku)
                if not producto:
                    print(f"Producto con SKU {sku} no encontrado.")
                    continue
                print("Deje en blanco los campos que no desea actualizar.")
                marca = input(f"Marca actual ({producto.get_marca()}): ") or producto.get_marca()
                modelo = input(f"Modelo actual ({producto.get_modelo()}): ") or producto.get_modelo()
                precio = input(f"Precio actual ({producto.get_precio()}): ") or producto.get_precio()
                stock = input(f"Stock actual ({producto.get_stock()}): ") or producto.get_stock()
                producto.set_marca(marca)
                producto.set_modelo(modelo)
                producto.set_precio(float(precio))
                producto.set_stock(int(stock))
                product_service.update_product(producto)
                print("Producto actualizado exitosamente.")
            elif opcion == "5":
                sku = input("Ingrese el SKU del producto a eliminar: ")
                product_service.delete_product(sku)
                print("Producto eliminado exitosamente.")
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except Exception as e:
            print(f"Error: {e}")

def menu_pedidos():
    while True:
        print("\n--- Menú Pedidos ---")
        print("1. Crear pedido")
        print("2. Ver pedidos")
        print("3. Buscar pedidos por RUT")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                rut = input("Ingrese el RUT del cliente: ")
                cliente = client_service.get_client_by_rut(rut)
                if not cliente:
                    print(f"Cliente con RUT {rut} no encontrado.")
                    continue
                pedido = Pedido()
                pedido.set_cliente_rut(rut)
                pedido.set_cliente_nombre(cliente.get_name())
                productos = []
                while True:
                    sku = input("Ingrese el SKU del producto (o presione Enter para finalizar): ")
                    if not sku:
                        break
                    producto = product_service.get_product_by_sku(sku)
                    if not producto:
                        print(f"Producto con SKU {sku} no encontrado.")
                        continue
                    cantidad = int(input(f"Ingrese la cantidad para el producto '{producto.get_modelo()}': "))
                    productos.append({"sku": sku, "cantidad": cantidad, "precio_unitario": producto.get_precio()})
                pedido.set_productos(productos)
                pedido.set_total(sum(p["cantidad"] * p["precio_unitario"] for p in productos))
                pedido.set_estado(input("Ingrese el estado del pedido (pendiente/completado): "))
                order_service.add_order(pedido)
                print("Pedido creado exitosamente.")
            elif opcion == "2":
                pedidos = order_service.get_all_orders()
                datos = []
                for pedido in pedidos:
                    productos = ", ".join([f"{p['sku']} x{p['cantidad']}" for p in pedido.get_productos()])
                    datos.append([pedido.get_cliente_rut(), pedido.get_cliente_nombre(), productos, pedido.get_total(), pedido.get_estado()])
                encabezados = ["RUT Cliente", "Nombre Cliente", "Productos", "Total", "Estado"]
                mostrar_tabla(datos, encabezados)
            elif opcion == "3":
                rut = input("Ingrese el RUT del cliente: ")
                pedidos = order_service.get_orders_by_rut(rut)
                if not pedidos:
                    print(f"No se encontraron pedidos para el cliente con RUT {rut}.")
                    continue
                datos = []
                for pedido in pedidos:
                    productos = ", ".join([f"{p['sku']} x{p['cantidad']}" for p in pedido.get_productos()])
                    datos.append([pedido.get_cliente_rut(), pedido.get_cliente_nombre(), productos, pedido.get_total(), pedido.get_estado()])
                encabezados = ["RUT Cliente", "Nombre Cliente", "Productos", "Total", "Estado"]
                mostrar_tabla(datos, encabezados)
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except Exception as e:
            print(f"Error: {e}")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Clientes")
        print("2. Productos")
        print("3. Pedidos")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_pedidos()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()