'''Crea un programa que solicite al usuario ingresar el precio de un producto y la cantidad que desea comprar. Luego, aplica los siguientes descuentos:
Si el usuario compra más de 5 unidades del producto, se le otorga un descuento del 10%.
Si el usuario compra más de 10 unidades, se le otorga un descuento adicional del 5% sobre el descuento anterior.
Si el usuario compra más de 20 unidades, se le otorga un descuento adicional del 3% sobre el descuento total.
El programa debe calcular el precio final después de aplicar los descuentos y mostrarlo al usuario.
'''
precio=0
cantidad=0
precio= int(input("ingrese el precio del producto:"))
cantidad=int(input("ingrese la cantidad que desea comprar:"))
descuento1= (0.9)
descuento2=(0.85)
descuento3=(0.82)

if cantidad>=5:
    print("su total es", (precio*cantidad*descuento1),"y obtuvo un descuento del 10%")
    
if cantidad>=10:
    print("su total con descuento adicional es", (precio*cantidad*descuento2),"y obtuvo un descuento adicional del 5%, aparte del 10%")
    
if cantidad>=20:          
     print("su total con descuentos adicionales es", (precio*cantidad*descuento3),"y obtuvo un descuento adicional del 3%, aparte del 5% y 10%")