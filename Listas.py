lista = ["Jesus","David","Suarez","Baptista"]
print(f'Lista simple: {lista}')
#Imprimir un rango
print(f'Rango de lista: {lista[0:2]}')
#Ir al inicio de la lista al indice
print(f'Inicio de la lista: {lista[:2]}')
#Desde el indice indicado hasta el final de la lista
print(f'Indice seleccionado: {lista[1:]}')
#Cambiar un nuevo valor
lista [2] = 'Calderon'
print(f'Cambio de valor en la lista: {lista}')
#Cantidad de elementos que tiene la lista
print(f'Numero de elementos: {len(lista)}')
#Agregar un elemento
lista.append('Suarez')
print(f'Agregar un elemento: {lista}')
#Insertar un elemento en un indice en especifico
lista.insert(2,'Sol')
print(f'Agregar en especifico: {lista}')
#Remover un elemento
lista.remove('Sol')
print(f'Remover de la lista: {lista}')
# Remover el ultimo elemento de la lista
lista.pop()
print(lista)
# del -> delete (eliminar)
del lista [1]
print(f'{len(lista)} -> {lista}')
# limpiar lista
lista.clear()
print(lista)
# borrar la lista
# del lista
# print(lista)