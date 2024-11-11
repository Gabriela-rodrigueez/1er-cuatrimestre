#Realizar un programa que el usuario ingrese n y el programa muestre cuantos numeros pares hay de 1 hasta n incluido

n=0
n=int(input("ingrese un numero: "))
for calcular in range(n):
    if calcular %2==0:
        print(calcular)