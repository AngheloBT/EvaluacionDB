from abc import ABC, abstractmethod

class Connection(ABC):
    @abstractmethod
    def execute(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def fetchone(self):
        pass

    @abstractmethod
    def fetchall(self):
        pass

    @abstractmethod
    def get_last_row_id(self):
        pass
