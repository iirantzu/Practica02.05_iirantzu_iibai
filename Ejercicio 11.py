#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos
#listas y muestre por pantalla su producto escalar.

vector_a = (1, 2, 3)
vector_b = (-1, 0, 2)
producto_escalar = 0
for a in range(len(vector_a)):
   producto_escalar += vector_a[a]*vector_b[a]
print("El producto escalar de los vectores " + str(vector_a) + " y " + str(vector_b) + " es " + str(producto_escalar))