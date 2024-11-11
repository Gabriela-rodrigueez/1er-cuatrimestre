# El usuario ingresa un numero del 1 al 7. Determinar qué día de la semana corresponde el dia ingresado. Ejemplo: si ingresa 7 muestra "Domingo")

dia= int(input("ingrese un numero del 1 al 7:"))

if dia==1:
    print("Es Lunes")
    
if dia==2:
        print("Es Martes")
        
if dia==3:
        print("Es Miercoles")
        
if dia==4:
        print("Es Jueves")
        
if dia==5:
        print("Es Viernes")
        
if dia==6:
        print("Es Sabado")

if dia==7:
    print("Es Domingo")

else:
    print("No corresponde a ningun dia")
