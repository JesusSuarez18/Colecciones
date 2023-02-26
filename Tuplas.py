frutas = ('Naranja','Plátano','Guabaya')
print(f'Tupla simple: {frutas}')
#Elementos de una tupla
print(len(frutas))
#Acceder un elemento
print(frutas[1])
#Rango de elementos
print(frutas[0:2])#Sin incluir el ultimo elemento
for fruta in frutas:
    print(fruta)
'''Modificar una tupla:
    Tupla -> lista -> modificar el elemento -> reasignar la lista a tupla
    
    Nota: "frutas [0] = 'Pera'" # Esto no se puede realizar, ya que ocasiona un error
'''
Fruta_Lista = list(frutas)
Fruta_Lista [0] = 'Pera'
frutas = tuple(Fruta_Lista)
print(frutas)
#Eliminar la tupla
del frutas
print(frutas)