#SET
planetas = {'Marte','Jupiter','Venus'}
print(planetas)
# Elementos del set
print(len(planetas))
# revisar si un elemento esta presente
print('Mercurio' in planetas)
#agregar elementos
planetas.add('Tierra')
print(planetas)
#Eliminar un elemento, remove -> elimina con errores. Discard -> elimina sin errores
planetas.remove('Tierra')
print(planetas)
planetas.discard('Jupiters')
print(planetas)
#limpieza
planetas.clear()
print(planetas)
#eliminar
del planetas
print(planetas)