#6 Pedir al usuario ingrese 3 notas de Programacion y calcule el promedio obtenido y decir si aprobó o No aprobó (se aprueba con 6)
nota1=0
nota2=0
nota3=0
nota1=int(input("ingrese la primera nota de programacion: "))
nota2=int(input("ingrese la segunda nota: "))
nota3=int(input("ingrese la tercera nota: "))

promedio = (nota1+nota2+nota3)/3
print("el promedio de programacion es: ", promedio)

if promedio>=6.0:
    print("aprobado")
else:
    print("desaprobado")