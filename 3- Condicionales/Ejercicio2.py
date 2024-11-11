# Vas a comprar chocolates en oferta, cada uno vale $325, comprando 5 o mas tienen un descuento del 10%.
# Si compras 10 o mas tienen un descuento del 17%, si compras 20 o mas tienen un descuento del 30%.
# Crear un programa que reciba la cantidad de chocolates que queres comprar y devuelva el precio final.

precio=325
chocolate=0
chocolate=int(input("cuantos chocolates va a querer:"))
descuento1= (0.9)
descuento2= (0.83)
descuento3= (0.7)


if chocolate>=5:
    print ("su total es" ,(precio*chocolate*descuento1),"y tuvo en descuento del 10%")
    
elif chocolate>=10:
    print ("su total es",(precio*chocolate*descuento2),"y tuvo en descuento del 17%")
    
elif chocolate>=20:
    print("su total es",(precio*chocolate*descuento3),"y tuvo en descuento del 30%")
    
else:
    print("no tiene descuento")