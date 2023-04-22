class Fresa:
    #contructor
    def __init__(self):
        self.__nombre = None
        self.__cantidad = None
        self.__precio = None
        self.__vitaminaAportada = None

    #declarondo GET (OBTENGO/MUESTRO UN ATRIBUTO)
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def vitaminaAportada(self):
        return self.__vitaminaAportada

    #declarando el SET (CONFIGURO,LLEVO UN VALOR AL ATRBUTO)
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato
    
    @cantidad.setter
    def cantidad(self,dato):
        print("La cantidad es: ")

    @precio.setter
    def precio(self,dato):
        print("La cantidad es: ")
    
    @vitaminaAportada.setter
    def vitaminaAportada(self,dato):
        print("La cantidad es: ")

    def agregarFruta(self):
        print("Se pica y se macera con azucar morena")    
