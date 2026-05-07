#Los diccionarios son parejas clave:valor
usuarios= {'user1':'login1', 'user2':'login2', 'user3':'login3', 'user4':'login4'}
print("usuarios:", usuarios)

#Si accedo a una clave obtengo su valor
print("usuarios[user1]:", usuarios['user1'])
print("usuarios[user2]:", usuarios.get('user2'))

print("usuarios.keys:", usuarios.keys())
print("usuarios.values:", usuarios.values())

#Obtener la cadena resultante de concatenar todos los valores
resul=''
for i in usuarios.values():
    resul += ' ' + i

print("resul:", resul)


#Se pueden añadir nuevos elementos al diccionario
usuarios['user5']='login5'
print("usuarios:", usuarios)


#Se pueden modificar los elementos del diccionario
usuarios['user2']='Login2'
print("usuarios:", usuarios)


#Se pueden eliminar elementos del diccionario
del(usuarios['user5'])
print("usuarios:", usuarios)
exit(0)