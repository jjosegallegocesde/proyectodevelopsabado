class  Borojo:
    def __init__(self):
        self.__nombre=None
        self.__cantidad = None
        self.__precio = None
        self.__vitaminaaportada = None

    #declarando el metodo GET  (OBTENGO /MUESTRA UN ATRIBUTO)
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
    def vitaminaaportada (self):
        return self.__vitaminaaportada
    
   
    #declarando el metodo SET  (CONFIGURO ,LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,dato):
        self.__nombre = dato

    @cantidad.setter
    def cantidad(self,dato):
        self.__cantidad = dato    

    @precio.setter
    def precio (self,dato):
        self.__precio= dato 

    @vitaminaaportada.setter
    def vitaminaaportada  (self,dato):
        self.__vitaminaaportada = dato       

    def agregarFruta(self):
        print("se le quita la bolsa y le echa leche")