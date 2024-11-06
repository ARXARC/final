ecosistema = {}
while True:
    especie = input("Ingrese el nombre de una especie avistada (o 'fin' para terminar): ")    
    if especie.lower() == 'fin':
        break
    if especie in ecosistema:
        ecosistema[especie] += 1
    else:
        ecosistema[especie] = 1
distribucion = collections.Counter(ecosistema)
print("\nInforme de avistamientos:")
for especie, cantidad in distribucion.items():
    print(f"{especie}: {cantidad} avistamientos")
especie_mas_comun = distribucion.most_common(1)[0][0]
cantidad_mas_comun = distribucion.most_common(1)[0][1]
print(f"\nLa especie más común en el ecosistema es '{especie_mas_comun}' con {cantidad_mas_comun} avistamientos.")
print("\nGracias por utilizar el programa de monitoreo de especies en un ecosistema.")
