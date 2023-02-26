#Diccionarios (Key, value)

diccionario = {'IDE': 'Integrated Development Environment',
               'OOP': 'Object Oriented Programming',
               'DBMS': 'Database Management System'}
print(diccionario)
#Largo del elemento
print(len(diccionario))
#acceder a un elemento
print( diccionario['IDE'])
print(diccionario.get('OOP'))
#Recorrer los elementos
# for termino,valor in diccionario.items():
#     print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#Limpiar el diccionario
diccionario.clear()
print(diccionario)

#Elimimar el diccionario
del diccionario
print(diccionario)