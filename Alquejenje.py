class Alquejenje:
    def __init__(self):
        self.__nombre = None
        self.__cantidad = None
        self.__precio=None
        self.__vitaminaAportada=None
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, data):
        self.__nombre=data

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, data):
        self.__cantidad=data

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, data):
        self.__precio=data

    @property
    def vitaminaAportada(self):
        return self.__vitaminaAportada
    
    @vitaminaAportada.setter
    def vitaminaAportada(self, data):
        self.__vitaminaAportada=data

    
    def agregarFruta(self):
        print(f'Se pica y se macera con azucar morena')