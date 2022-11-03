#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

premio = []

for gandores in range(4):
    num_loteria = int(input("Introduzca el número ganador de la lotería: "))
    premio.append(num_loteria)
    premio.sort()

print("Los números gandores de la loteria son: " + str(premio))