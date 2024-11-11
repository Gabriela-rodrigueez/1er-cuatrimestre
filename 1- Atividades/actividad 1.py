radio=0
radio=int(input("escriba el radio:"))
def calcular(area):
    area= 3.14* radio ** 2
    return area    


area=calcular(radio)
print(f"el area es {area}")

