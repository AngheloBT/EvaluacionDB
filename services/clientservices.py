from repositories.clientrepository import ClientRepository
from models.client import Client
from typing import List, Optional

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def add_client(self, client: Client) -> Client:
        self._verificar_no_existencia(client.get_id())
        return self.client_repository.add_client(client)

    def get_client_by_id(self, client_id: int) -> Optional[Client]:
        return self.client_repository.get_client_by_id(client_id)

    def get_client_by_email(self, email: str) -> Optional[Client]:
        return self.client_repository.get_client_by_email(email)

    def update_client(self, client: Client) -> None:
        self._verificar_existencia(client.get_id())
        self.client_repository.update_client(client)

    def delete_client(self, client_id: int) -> None:
        self._verificar_existencia(client_id)
        self.client_repository.delete_client(client_id)

    def get_all_clients(self) -> List[Client]:
        return self.client_repository.show_all_clients()

    def _verificar_existencia(self, client_id: int) -> None:
        if not self.client_repository.get_client_by_id(client_id):
            raise ValueError(f"Cliente con ID {client_id} no existe.")

    def _verificar_no_existencia(self, client_id: int) -> None:
        if self.client_repository.get_client_by_id(client_id):
            raise ValueError(f"Cliente con ID {client_id} ya existe.")
