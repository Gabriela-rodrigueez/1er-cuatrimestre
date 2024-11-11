'''Escribir un programa que ingrese 5 números por teclado y muestre el mayor.Usar bucle for'''

numero=0
auxiliar=0
for contador in range(5):
    numero=int(input("ingrese un numero:"))
    if numero>auxiliar:
        auxiliar=numero
print("el numero mayor es:", auxiliar)