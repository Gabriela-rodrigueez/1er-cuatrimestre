#Simularemos el juego de preguntados para dos jugadores.
# Cada jugador tendrá su turno.
# Antes de comenzar los jugadores ingresarán sus nombres para que el
# programa diga a quien corresponde el turno por su nombre.
# Deberemos guardar listas con los nombres y preguntas divididas en categorias
# o categorías. [(]al menos tres categorías)
# Aleatoriamente el programa elegirá una pregunta de acuerdo a la categoría
# seleccionada y si el usuario responde correctamente le sumara 100 puntos. 
# Gana el jugador que llega primero a los 1.000 puntos

import random
print("Bienvenido al juego del Preguntado trucho")
jugador1= input("Ingrese su nombre Jugador 1: ")
jugador2= input("Ingrese su nombre Jugador 2: ")
puntaje_jugador1=0
puntaje_jugador2=0

categorias= {
    "Geografia": ["¿En qué continente está Tasmania?", "Oceania"],
    "Ciencia": ["¿Cuál es el simbolo del Helio?","He"],
    "Historia": ["¿De qué nacionalidad era Karl Marx?","Aleman"],
    "Arte": ["¿De qué país son originarios Los Beatles?","Inglaterra"],
    "Deportes": ["¿En qué superficie se juega al waterpolo?","En el agua"],
    "Entretenimiento": ["¿De qué color es el auto que usa Homero Simpson?","Rosa"]
}


def elegir_pregunta():
    participantes=random.choice([jugador1, jugador2])
    print(participantes)
    categoria= random.choice(list(categorias.keys()))
    pregunta, respuesta = categorias[categoria]
    return categoria, pregunta, respuesta

def validacion(respuesta_correcta, respuesta_jugador):
    return respuesta_correcta.lower()== respuesta_jugador.lower()

def mostrar_puntaje():
    print(f"{jugador1}: {puntaje_jugador1} puntos")
    print(f"{jugador2}: {puntaje_jugador2} puntos")
    
while True:
    categoriaA, preguntaA, respuestaA = elegir_pregunta()
    print(f"\nCategoría: {categoriaA}")
    print(f"Pregunta: {preguntaA}")
    respuesta_jugador= input("Respuesta: ")
    
    if validacion(respuestaA, respuesta_jugador):
        print("La Respuesta es correcta. Suma 100 puntos")
        if random.choice([True, False]):
            puntaje_jugador1 += 100
                       
        else:
            print("La Respuesta es incorrecta. Espere su turno para volverlo a intentar ")
            
    mostrar_puntaje()
    
    if puntaje_jugador1>= 1.000 or puntaje_jugador2>=1.000:
        ganador= jugador1 if puntaje_jugador1>=1.000 else jugador2
        print(f"\n{ganador} ha ganado.")
        print("Fin del juego. Hasta pronto")
        break