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
        #Declarando el metodo SET (configuro, llevo un valor a un atributo)
        @nombre.setter
        def nombre(self,dato):
            self.__nombre=dato


    def agregarFruta(self):
        print ("Se raspa y se tira a lo mas despreciable")