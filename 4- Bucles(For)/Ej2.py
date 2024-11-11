#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
# desde 1 hasta ese número separados por comas.


numero=0
numero=int(input("ingrese un numero entero y positivo:"))
for contador in range(numero):
    if contador %2!=0:
        print(contador, ",")
print(numero)