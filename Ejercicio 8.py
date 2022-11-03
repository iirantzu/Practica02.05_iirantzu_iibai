#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
#letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

palabra1 = input("Introduce una palabra: ")
inversa = palabra1
palabra = list(palabra1)
inversa = list(inversa)
inversa.reverse()
if palabra == inversa:
   print("La palabra " + palabra1 + " es un palíndromo")
else:
   print("La palabra " + palabra1 + " no es un palíndromo")