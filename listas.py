colores=[] #Lista vacia
colores=["rojo","verde","azul"] #Lista con 3 elementos
print("Colores:",  colores)
print("Colores[0]:", colores[0]) #Acceder al primer elemento

colores[0]='Blanco' #Modificar el primer elemento
print(f"colores: {colores}, colores[0]: {colores[0]}") #Imprimir la lista y el primer elemento

colores.append("Amarillo") #Agregar un nuevo elemento al final de la lista
print("Colores:", colores)

for i in colores:
    print(i) #Imprimir cada color en la lista

coloresMin=[ i.lower() for i in colores] #Crear una nueva lista con los colores en minúscula
print("Colores en minúscula:", coloresMin)

print("Colores: ", colores)
col=input("Dime un color: ")#Pedir al usuario que ingrese un color
pos= colores.index(col) #Buscar la posición del color ingresado en la lista
print(f"Color indicado {col}, posición en la lista: {pos}")

try:
    pos= colores.index(col) #Buscar la posición del color ingresado en la lista
    print(f"Color indicado {col}, posición en la lista: {pos}")
except Exception as e:
    print(f"El color {col} no se encuentra en la lista de colores.")

print("La ejecución del programa continúa")