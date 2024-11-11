suma=0
for contador in range (10):
    numero=int (input("ingrese un numero:"))
    suma +=numero
    if numero %2==0:
        print("la suma de los numeros pares es:",(suma))
else: 
    print("fin")