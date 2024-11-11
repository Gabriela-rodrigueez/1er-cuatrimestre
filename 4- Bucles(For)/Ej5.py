#Ingresar 10 números por pantalla. Mostrar solo los impares.

numero=0
for contador in range(10):
    numero=int(input("ingrese un numero:"))
    if numero %2!=0:
        print(numero)
        