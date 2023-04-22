class Durazno:
    def __init__(self):
        self.__nombre = None
        self.__cantidad = None
        self.__precio = None
        self.__vitanmina = None
    #declarando el metodo get(obtengo un atributo)
    @property
    def nombre(self):
        return self.__nombre
    #declarando el metodo set(llevo un valor a un atributo)
    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato 
        
    @property
    def cantidad(self):
        return self.__nombre
    @cantidad.setter
    def cantidad(self, dato):
        self.__cantidad = dato 
    
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, dato):
        self.__precio = dato
        
    @property
    def vitanmina(self):
        return self.__vitanmina
    @vitanmina.setter
    def vitanmina(self, dato):
        self.__vitanmina = dato
    
    def agregarFrua(self):
        print("se pica y se hecha se macera con azucar")
        
   