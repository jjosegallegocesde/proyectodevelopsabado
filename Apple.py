class Apple:              #para poner un atributo privado es la siguiente forma __
    def __init__(self):
      self.__nombre=None
      self.__cantidad=None
      self.__precio=None
      self.__vitaminaAportada=None

    #DECLARANDO EL METODO GET (OBTENGO/MUESTRO UN ATRIBUTO)
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
    
    #DECLANDO EL METODO SET (CONFIGURO, LLEVO UN VALOR A UN ATRIBUTO.)

    @vitaminaAportada.setter
    def vitaminaAportada(self,dato):
       self.__vitaminaAportada=dato

    @precio.setter
    def precio(self,dato):
       self.__precio=dato

    @cantidad.setter
    def cantidad(self,dato):
       self.__cantidad=dato

    @nombre.setter
    def nombre(self,dato):
       self.__nombre=dato


    def agregarFruta():
       print('Se pica y se macera con azucar morena',)

