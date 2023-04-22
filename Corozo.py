class Corozo:

    def __init__(self):
        self.__nombre=None
        self.__cantidad=None
        self.__precio=None
        self.__vitaminaAportada=None
    
    #Declarando el metodo GET (obtengo/muestro un atributo)
    @property    
    def nombre(self):
        return self.__nombre
    
    #Declarando el metodo SET (configuro, llevo un valor a un atributo)
    @nombre.setter
    def nombre(self,dato):
        self.__nombre=dato
    
    @property    
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self,dato):
        self.__cantidad=dato
    
    @property    
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,dato):
        self.__precio=dato

    @property    
    def vitaminaAportada(self):
        return self.__vitaminaAportada

    @vitaminaAportada.setter
    def vitaminaAportada(self,dato):
        self.__vitaminaAportada=dato












    def agregarFruta(self):
        print('Se le quita la concha, se mezcla con agua y azucar monera')