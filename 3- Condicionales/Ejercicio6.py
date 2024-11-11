# Juego de Adivinanza
# Crea un programa en Python que le pida al usuario adivinar un número secreto. El programa debe seguir los siguientes pasos:
# Pide al usuario que ingrese un número.
# Compara el número ingresado por el usuario con el número secreto (lo elige el programador).
# Si el número ingresado es igual al número secreto, muestra un mensaje de felicitación y termina el juego.
# Si el número ingresado es mayor o menor que el número secreto, muestra un mensaje indicando si el número secreto es mayor o menor.


numero=0
numero=int(input("ingrese un numero:"))
numero_secreto= 68

if numero==numero_secreto:
    print("felicitaciones, adivino el numero secreto")

elif numero>numero_secreto:
    print("el numero secreto es menor")
    
elif numero<numero_secreto:
    print("el numero secreto es mayor") 
       
else:
    print("no adivino el numero secreto")