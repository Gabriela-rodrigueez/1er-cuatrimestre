'''En una empresa se le paga al personal un bono según los años que llevan en la misma.
Si la persona lleva 5 años o menos el bono es de $5.000, mas de 5 años y menos de 20 años es de $10.000, mas de 20 años, el bono es de $15.000.
Crear un programa que reciba el nombre del empleado y los años que lleva en la empresa y devuelva el bono que le corresponde.
Debe retornar el nombre del empleado junto con la palabra "tiene un bono de" y el valor del bono. 
Ejemplo: "Pedro tiene un bono de 10000"
'''
nombre=0
años=0
nombre=input("Ingrese su nombre:")
años=int(input("ingrese los años que lleva en la empresa:"))

if años<=5:
    print(f"{nombre} recibira un bono de $5.000")
    
elif años>=5 and años<=20:
    print(f"{nombre} ricibira un bono de $10.000")

elif años>=20:
    print(f"{nombre} recibira un bono de $15.000")
    
else:
    print(f"{nombre} no recibira ningun bono")