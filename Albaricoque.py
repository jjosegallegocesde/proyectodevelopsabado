class Mora:
  def __init__(self):
    self.__nombre=None
    self.__cantidad=None
    self.__precio=None
    self.__vitamonaAportada=None
    
    #DECLARACION DE METODOS GET Y SET
    @property
    def nombre(self):
      return self.__nombre
    
    @property
    def cantidad(self):
      return self.__cantidad
    
    
    
    #DECLARANDO EL SET
    @nombre.setter
    def nombre(self,dato):
      self.__nombre=dato
      
    @cantidad.setter
    def cantidad(self,dato):
     self.__cantidad=dato
    
    def agregarFruta(self):
      print("se pica , se macera y se corta")