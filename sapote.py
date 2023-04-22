class sapote:
    def __init__(self):
        self.__nombre=None
        self.__cantidad=None
        self.__precio=None
        self.__vitaminaApor=None
    
    @property
    def nombre (self):
        return self.__nombre
    @property
    def cantidad(self):
        return self.__cantidad
    
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato
    
    @cantidad.setter
    def cantidad(self,dato):
        self.cantidad.dato

    def agregarFruta(self):
        print("se pica y se macera con azucar morena")