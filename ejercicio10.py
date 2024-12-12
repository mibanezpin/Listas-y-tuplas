precios = [50, 75, 46, 22, 80, 65, 8]
minimo = maximo = precios[0]
for precio in precios:
    if precio < minimo:
        minimo = precio
    elif precio > maximo:
        maximo = precio 
print("El minimo es " + str(minimo)) 
print("El maximo es " + str(maximo))