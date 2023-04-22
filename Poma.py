class Poma:
    def __init__(self):
        self.__nombre=None
        self.__cantidad=None
        self.__precio=None
        self.__vitaminaAporta=None

        #DECLARANDO DEL METODO GET CON EL GET OBTENGO  Y MUESTRO UN ATRIBUTO
        @property
        def nombre(self):
            return self.__nombre
        
        #DECLARANDO EL METODO SET CONFIGURO Y LLEVO EL VALOR A UN ATRIBUTO
        @nombre.setter
        def nombre(self,dato):
            self.__nombre=dato

    def agregarFruta(self):
        print("Se pica y se hecha con azúcar morena")

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
        def VitaminaAporta(self):
            return self.__VitaminaAporta

        @VitaminaAporta.setter
        def VitaminaAporta(self,dato):
            self.__VitaminaAporta=dato



