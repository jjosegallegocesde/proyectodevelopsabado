class pitahaya:
    def __init__(self):
        self.__nombre=None
        self.__cantidad=None
        self.__precio=None
        self.__vitaminaAportada=None

#DECLARANDO METODO GET (OBTEMGO/MUESTRO UN ATRIBUTO)
    @property
    def nombre(self):
        return self.__nombre
    
    #DECLARANDO EL METODO SELF (CONFIGURO,LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,dato):
        self.__nombre = dato

    def agregarFruta(self):
        print("se pica y se macera con azucar")

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,dato):
        self.__cantidad = dato

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,dato):
        self.__precio= dato

    @property
    def vitaminaAportada(self):
        return self.__vitaminaAportada
    
    @vitaminaAportada.setter
    def vitaminaAportada(self,dato):
        self.__vitaminaAportada = dato

