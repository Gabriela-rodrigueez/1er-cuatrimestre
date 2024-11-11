while (True):
    print("Bienvenido al juego")
    juego=input("ingrese Piedra, Papel o Tijera: ")
    print(juego)
    import random
    aleatorio=random.choice(['Piedra','Papel','Tijera'])
    print(aleatorio)
   

    if (juego==aleatorio):
        print("Empate")
    elif (juego=='Piedra' and aleatorio=='Tijera')or\
        (juego=='Papel' and aleatorio=='Piedra')or\
        (juego=='Tijera' and aleatorio=='Papel'):
        print("Ganaste")
    else:
        print("Perdiste")
    juegador=input("¿Quieres volver a jugar?")
    if (juegador!='si'):
        break