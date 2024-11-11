#Mostrar la tabla de multiplicar de un n numero ingresado por teclado.

numero=int(input("Ingrese un numero para obtener su tabla de multiplicar: "))

for x in range(1,11):
    resultado = numero * x
    print(f"{numero} x {x} = {resultado} ")