class Product:
    def __init__(self):
        self.__sku: str = ""         
        self.__marca: str = ""
        self.__modelo: str = ""
        self.__precio: float = 0.0
        self.__stock: int = 0

    def get_sku(self): 
        return self.__sku
    
    def set_sku(self, sku: str): 
        self.__sku = sku

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca: str): 
        self.__marca = marca

    def get_modelo(self): 
        return self.__modelo
    
    def set_modelo(self, modelo: str): 
        self.__modelo = modelo

    def get_precio(self): 
        return self.__precio
    
    def set_precio(self, precio: float): 
        self.__precio = precio

    def get_stock(self): 
        return self.__stock
    
    def set_stock(self, stock: int): 
        self.__stock = stock
        

    def to_dict(self) -> dict:
        return {
            "sku": self.__sku,
            "marca": self.__marca,
            "modelo": self.__modelo,
            "precio": self.__precio,
            "stock": self.__stock
        }

    def from_dict(self, data: dict):
        self.__sku = data.get("sku", "")
        self.__marca = data.get("marca", "")
        self.__modelo = data.get("modelo", "")
        self.__precio = data.get("precio", 0.0)
        self.__stock = data.get("stock", 0)
