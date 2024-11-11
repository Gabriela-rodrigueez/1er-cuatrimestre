#4. Pedir al usuario ingrese un numero y verificar si es par y mayor que 100
num=0
num= int(input("ingresar un numero: "))
if num%2==0:
    print("es par")
else:
    print("es impar") 
    
if num>=100:
    print("y mayor a 100")
else:
    print("y menor a 100")