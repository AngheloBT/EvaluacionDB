from repositories.clientrepository import ClientRepository
from models.client import Client
from typing import List, Optional

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def add_client(self, client: Client) -> Client:
        self._verificar_no_existencia(client.get_rut())
        return self.client_repository.add_client(client)

    def get_client_by_rut(self, rut: str) -> Optional[Client]:
        return self.client_repository.get_client_by_rut(rut)

    def get_client_by_email(self, email: str) -> Optional[Client]:
        return self.client_repository.get_client_by_email(email)

    def update_client(self, client: Client) -> None:
        self._verificar_existencia(client.get_rut())
        self.client_repository.update_client(client)

    def delete_client(self, rut: str) -> None:
        self._verificar_existencia(rut)
        self.client_repository.delete_client(rut)

    def get_all_clients(self) -> List[Client]:
        return self.client_repository.show_all_clients()

    def _verificar_existencia(self, rut: str) -> None:
        if not self.client_repository.get_client_by_rut(rut):
            raise ValueError(f"Cliente con RUT {rut} no existe.")

    def _verificar_no_existencia(self, rut: str) -> None:
        if self.client_repository.get_client_by_rut(rut):
            raise ValueError(f"Cliente con RUT {rut} ya existe.")