import random

contador=0
aleatorio=random.randint(1,100)
while (contador<5):
    
    numero=int(input("ingrese un numero:"))
    
    if numero==aleatorio:
        print("felicitaciones, adivino el numero secreto")
        break

    elif numero>aleatorio:
        print("el numero secreto es menor")
        
    elif numero<aleatorio:
        print("el numero secreto es mayor") 
        
    else:
        print("no adivino el numero secreto")
        break
