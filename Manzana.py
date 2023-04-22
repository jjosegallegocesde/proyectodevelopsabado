class Manzana:
    def __init__(setf):
     setf.__nombre=None
     setf.__cantidad=None
     setf.__precio=None
     setf.__victamnaAportada=None

    #declarando el metodo get (obtengo/ muestro un atributo) 
    @property
    def nombre(setf):
       return setf.__nombre
    
    @property
    def cantidad(self):
       return self.__cantidad
    
    #declarando el metodo set (configuro , llevo un valor a un atributo)
    @nombre.setter
    def nombre(setf,dato):
       setf.__nombre=dato

    @cantidad.setter
    def cantidad(setf,dato):
       setf._nombre=dato
    
    def agregarfruta(self):
       print('se pica y se macera con azucar')