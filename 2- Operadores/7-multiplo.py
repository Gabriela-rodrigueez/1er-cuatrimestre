#7. Pedir al usuario ingrese un numero y verifique si es multiplo de 4 y de 100 al mismo tiempo
num=0
num=int(input("ingrese un numero: "))
if num%4==0:
    print("es multiplo de 4")
else:
    print("no es multiplo de 4")
    
if num%100==0:
    print("y es multiplo de 100")
else:
    print("y no es multiplo de 100")