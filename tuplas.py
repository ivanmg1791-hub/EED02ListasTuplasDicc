tupla1= (1, 2, 3, 'A', 'B', 'C')

#Tienen el mismo comportamiento que las listas
print("tupla1:", tupla1)
print("tupla1[0]:",tupla1[0])
print("tupla1Letras:", tupla1[3:])
print("tupla1Letras:", tupla1[-1:-4:-1])

#Las tuplas no permiten modificar los elementos
#tupla1[0]= 10 #Daría error

#Tampoco permiten el borrado de elementos de la tupla
#del(tupla1[0]) #Daría error

tupla2 = tuple(i for i in range(10))
print("tupla2: ", tupla2)

tupla3 = tuple(i for i in range(5,10))
print("tupla3: ", tupla3)

tupla3 = tuple(i for i in range(0,10,2))
print("tupla3: ", tupla3)

tupla4 = tuple(i for i in range(10) if i%3 == 0)
print("tupla4: ", tupla4)