#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha
#sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
#has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
#cada una de las correspondientes notas introducidas por el usuario.

lista_modulos = ["DAPI", "SIPA", "RETE", "GPIT", "EIEM", "SIRC"]
notas = []

for modulo1 in lista_modulos:
    nota = float(input("Cuánto has sacado en " + modulo1 + ":\n"))
    notas.append(nota)

for modulo2 in range(len(lista_modulos)):
    print("En " + lista_modulos[modulo2] + " has sacado un " + str(notas[modulo2]))