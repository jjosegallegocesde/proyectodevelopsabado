class Chilacuan: 
    def __init__(self):
        self.__nombre = None
        self.__cantidad = None
        self.__precio = None
        self.__vitaminaAportada = None
    
    # NOMBRE     
    # declarar metodo get  
    @property 
    def nombre(self):
        return self.__nombre
    
    # declarando metodo set 
    
    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato
    
    # CANTIDAD     
    # declarar metodo get  
    @property 
    def cantidad(self):
        return self.__cantidad
    
    # declarando metodo set 
    
    @cantidad.setter
    def cantidad(self, dato):
        self.__cantidad = dato
        
    # PRECIO     
    # declarar metodo get  
    @property 
    def precio(self):
        return self.__precio
    
    # declarando metodo set 
    
    @precio.setter
    def precio(self, dato):
        self.__precio = dato
        
    # VITAMINA      
    # declarar metodo get  
    @property 
    def vitaminaAportada(self):
        return self.__vitaminaAportada
    
    # declarando metodo set 
    
    @vitaminaAportada.setter
    def vitaminaAportada(self, dato):
        self.__vitaminaAportada = dato
    
    def agregarFruta(self):
        print("se pica y se echa")
    