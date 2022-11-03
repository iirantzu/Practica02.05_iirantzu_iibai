#Escribir un programa que pregunte por una muestra de números, separados por comas, los
#guarde en una lista y muestre por pantalla su media y desviación típica.

frase = input("Introduce una muestra de números separados por comas: \n")
frase = frase.split(',')
numero = len(frase)
for i in range(numero):
   frase[i] = int(frase[i])
frase = tuple(frase)
suma = 0
suma2 = 0
for i in frase:
   suma += i
   suma2 += i**2
media = suma/numero
desviacion_tipica = (suma2/numero-media**2)**(1/2)
print('La media es ' + str(media) + ', y la desviación típica es', str(desviacion_tipica))
