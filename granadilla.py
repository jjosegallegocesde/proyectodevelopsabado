class granadilla:

    def _init_(self):
        self.__nombre=None
        self.__cantidad=None
        self.__precio=None
        self.__vitaminaAportada=None

        #Declarando el metodo GET (Obtengo/muestro un atributo)
        @property
        def  nombre (self):
            return self.__nombre
        @property
        def cantidad (self):
            return self.__cantidad
        @property
        def precio (self):
            return self.__precio
        @property
        def vitaminaAportada (self):
            return self.__vitaminaAportada
        #Declarando el metodo SET (configuro, llevo un valor a un atributo)
        @nombre.setter
        def nombre(self,dato):
            self.__nombre=dato
        @cantidad.setter
        def cantidad(self,dato):
            self.__cantidad=dato
        @precio.setter
        def precio(self, dato):
            self.__precio=dato
        @vitaminaAportada.setter
        def vitaminaAportada(self, dato):
            self.__vitaminaAportada=dato


    def agregarFruta(self):
        print ("Se raspa y se tira a lo mas despreciable")