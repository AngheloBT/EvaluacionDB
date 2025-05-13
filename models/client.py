class Client:
    def __init__(self):
        self.__rut : str = ""
        self.__name : str = ""
        self.__email : str = ""
        self.__phone : int = 0
        self.__address : str = ""

    def get_rut(self) -> str:
        return self.__rut
    
    def set_rut(self, rut : str):
        self.__rut = rut

    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name : str):
        self.__name = name

    def get_email(self) -> str:
        return self.__email
    
    def set_email(self, email : str):
        self.__email = email
    
    def get_phone(self) -> int:
        return self.__phone
    
    def set_phone(self, phone : int):
        self.__phone = phone
    
    def get_address(self) -> str:
        return self.__address
    
    def set_address(self, address : str):
        self.__address = address