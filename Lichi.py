class Lichi:
    def __init__(self):
        self.__nombre = '';
        self.__cantidad = 0;
        self.__precio = 0;
        self.__vitaminas = 0;
        self.__proteinas = 0;
    
    #DECLARANDO EL METODO GET (OBTENGO/MUESTRO UN ATRIBUTO);
    @property
    def nombre(self):
        return self.__nombre;
    #DECLARANDO EL METODO SET (CONFIGURO, LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def cantidad(self):
        return self.__cantidad;
    #DECLARANDO EL METODO SET (CONFIGURO, LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,cantidad):
        self.__cantidad = cantidad
        
    @property
    def precio(self):
        return self.__precio;
    #DECLARANDO EL METODO SET (CONFIGURO, LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,precio):
        self.__precio = precio
        
    @property
    def vitaminas(self):
        return self.__vitaminas;
    #DECLARANDO EL METODO SET (CONFIGURO, LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,vitaminas):
        self.__vitaminas = vitaminas
        
    @property
    def vitaminas(self):
        return self.__proteinas;
    #DECLARANDO EL METODO SET (CONFIGURO, LLEVO UN VALOR A UN ATRIBUTO)
    @nombre.setter
    def nombre(self,proteinas):
        self.proteinas = proteinas
        
    
    def addFruit(self):
        print("Se pica y se licua con agua y leche y azucar blanca");
        
