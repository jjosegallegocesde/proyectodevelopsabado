class Nispero: 
    def __init__(self):
        self.__nombre = None  
        self.__cantidad = None
        self.__precio = None
        self.__vitaminaAportada = None

    @property    
    def nombre(self):
        return self.__nombre

    @nombre.setter     
    def nombre(self,dato):
        self.__nombre = dato

    @property    
    def cantidad(self):
        return self.____cantidad

    @cantidad.setter     
    def cantidad(self,dato):
        self.____cantidad = dato

    @property    
    def precio(self):
        return self.____precio

    @precio.setter     
    def precio(self,dato):
        self.____precio = dato
    
    @property    
    def vitaminaAportada(self):
        return self.____vitaminaAportada

    @vitaminaAportada.setter     
    def vitaminaAportada(self,dato):
        self.____vitaminaAportada = dato

    def agregarFruta(self): 
        print('se pica y se macera con azucar morena') 