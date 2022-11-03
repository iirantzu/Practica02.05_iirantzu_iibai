#Escribir un programa que almacene en una lista los siguientes precios, 50, 75,
#46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precio = [50, 75, 46, 22, 80, 65, 8]
minimo = maximo = precio[0]
for precio in precio:
   if precio < minimo:
       minimo = precio
   elif precio > maximo:
       maximo = precio
print("El precio mínimo es " + str(minimo))
print("El precio máximo es " + str(maximo))