#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha
#sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el
#programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["RETE", "SIHD", "DAPI", "EIEM", "GPIT", "SIPA", "SIRC"]
passed = []
for asignatura in asignaturas:
   nota = float(input("¿Cuanto has sacado en la asignatura " + subject + "?"))
   if nota >= 5:
       passed.append(asignatura)
for asignatura in passed:
   asignaturas.remove(asignatura)
print("La asignatura que tienes que repetir es " + str(asignaturas))