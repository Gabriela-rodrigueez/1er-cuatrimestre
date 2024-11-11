#Escriba un programa que reciba una cadena de texto y muestre cuantas vocales tiene la cadena, pueden ser mayusculas o minusculas

def contar(cadena):
    vocales=['a','e','i','o','u','á','é','í','ó','ú','ü']
    contador=0

    for letra in cadena2:
        if letra in vocales:
            contador +=1
    return contador


cadena=input("ingrese un texto: ")
cadena2= cadena.lower()
cantidad= contar(cadena)
print(f"La cadena tiene {cantidad} vocales")
