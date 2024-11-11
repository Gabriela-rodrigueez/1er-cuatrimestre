#Calcular y visualizar la suma y el producto de los números pares comprendidos entre 20 y 100

suma=0
producto= 1

for num in range(20, 101):
    if num %2==0:
        suma += num
        producto *= num
print(f"La suma de los numeros pares es: {suma}")
print(f"El producto de los numeros pares es: {producto}")