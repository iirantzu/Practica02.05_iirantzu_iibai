#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número
#de veces que contiene cada vocal.

palabra = input("Introduzca una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
   tiempo = 0
   for letra in palabra:
       if letra == vocal:
           tiempo += 1
   print("La vocal " + vocal + " aparece " + str(tiempo) + " veces")
