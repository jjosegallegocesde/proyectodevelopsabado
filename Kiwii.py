class Kiwii():
    def __init__(self):
        self.__nombre = None
        self.__cantidad = None
        self.__vitamina = None
        self.__precio = None

#declarando el metodo get (obtengo/muestro un atributo)
    @property
    def nombre(self):
        return self.__nombre
    @property
    def cantidad(self):
        return self.__cantidad
    @property
    def vitamina(self):
        return self.__vitamina
    @property
    def precio(self):
        return self.__precio
    
    #declarando el metodo set (configuro, llevoo un valor a un atributo)
    def nombre(self,dato):
        self.__nombre=dato
    def cantidad(self,dato):
        self.__cantidad=dato
    def vitamina(self,dato):
        self.__vitamina=dato
    def precio(self,dato):
        self.__precio=dato
    
    def agregarFruta(self):
        print("Se pica y se macera con azucar Morena")
