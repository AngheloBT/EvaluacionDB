from datetime import datetime,timezone

class Pedido:
    def __init__(self):
        self.__cliente_rut: str = ""
        self.__cliente_nombre: str = ""
        self.__productos: list = []  # Lista de dicts: {sku, cantidad, precio_unitario}
        self.__fecha: datetime = datetime.now(timezone.utc)
        self.__total: float = 0.0
        self.__estado: str = "pendiente"

    def get_cliente_rut(self): 
        return self.__cliente_rut
    
    def set_cliente_rut(self, rut: str): 
        self.__cliente_rut = rut

    def get_cliente_nombre(self): 
        return self.__cliente_nombre
    
    def set_cliente_nombre(self, nombre: str): 
        self.__cliente_nombre = nombre

    def get_productos(self): 
        return self.__productos
    
    def set_productos(self, productos: list): 
        self.__productos = productos

    def get_fecha(self): 
        return self.__fecha
    
    def set_fecha(self, fecha: datetime): 
        self.__fecha = fecha

    def get_total(self): 
        return self.__total
    
    def set_total(self, total: float): 
        self.__total = total

    def get_estado(self): 
        return self.__estado
    
    def set_estado(self, estado: str): 
        self.__estado = estado

    def to_dict(self) -> dict:
        return {
            "cliente_rut": self.__cliente_rut,
            "cliente_nombre": self.__cliente_nombre,
            "productos": self.__productos,
            "fecha": self.__fecha,
            "total": self.__total,
            "estado": self.__estado
        }

    def from_dict(self, data: dict):
        self.__cliente_rut = data["cliente_rut"]
        self.__cliente_nombre = data["cliente_nombre"]
        self.__productos = data["productos"]
        self.__fecha = data.get("fecha", datetime.now(timezone.utc))
        self.__total = data["total"]
        self.__estado = data.get("estado", "pendiente")
