# repositories/client_repository.py
from models.client import Client
from connections.sqlconnection import MySQLConnection
from typing import Optional, List

class ClientRepository:
    def __init__(self, connection: MySQLConnection):
        self.connection = connection

    def add_client(self, client: Client) -> Client:
        query = "INSERT INTO clientes (rut, nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)"
        self.connection.execute(query, (
            client.get_rut(),
            client.get_name(),
            client.get_email(),
            client.get_phone(),
            client.get_address()
        ))
        self.connection.commit()
        return client

    def get_client_by_rut(self, rut: str) -> Optional[Client]:
        query = "SELECT * FROM clientes WHERE rut = %s"
        self.connection.execute(query, (rut,))
        result = self.connection.fetchone()
        if result:
            client = Client()
            client.set_rut(result[0])
            client.set_name(result[1])
            client.set_email(result[2])
            client.set_phone(result[3])
            client.set_address(result[4])
            return client
        return None

    def get_client_by_email(self, email: str) -> Optional[Client]:
        query = "SELECT * FROM clientes WHERE email = %s"
        self.connection.execute(query, (email,))
        result = self.connection.fetchone()
        if result:
            client = Client()
            client.set_rut(result[0])
            client.set_name(result[1])
            client.set_email(result[2])
            client.set_phone(result[3])
            client.set_address(result[4])
            return client
        return None

    def update_client(self, client: Client) -> None:
        query = "UPDATE clientes SET nombre = %s, email = %s, telefono = %s, direccion = %s WHERE rut = %s"
        self.connection.execute(query, (
            client.get_name(),
            client.get_email(),
            client.get_phone(),
            client.get_address(),
            client.get_rut()
        ))
        self.connection.commit()

    def delete_client(self, rut: str) -> None:
        query = "DELETE FROM clientes WHERE rut = %s"
        self.connection.execute(query, (rut,))
        self.connection.commit()

    def show_all_clients(self) -> List[Client]:
        query = "SELECT * FROM clientes"
        self.connection.execute(query)
        results = self.connection.fetchall()
        clientes = []
        for row in results:
            client = Client()
            client.set_rut(row[0])
            client.set_name(row[1])
            client.set_email(row[2])
            client.set_phone(row[3])
            client.set_address(row[4])
            clientes.append(client)
        return clientes
