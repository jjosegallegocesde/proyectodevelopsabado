from Alquejenje import Alquejenje
from Nispero import Nispero

objeto=Alquejenje()

objeto.nombre="Alquejenje"
print(objeto.nombre)

objeto.cantidad=1
print(objeto.cantidad)

objeto.precio=5000
print(objeto.precio)


objeto= Nispero()
objeto.nombre='Nispero silvestre'
objeto.cantidad= '10'
objeto.precio = '1000'
objeto.vitaminaAportada= 'b1'
print(f'{objeto.nombre}, {objeto.cantidad}, {objeto.precio}, {objeto.vitaminaAportada}' )
