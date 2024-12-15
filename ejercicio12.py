
entrada = input("Escribe números separados por comas: ")

datos = [float(x) for x in entrada.split(",")]

num = len(datos)
suma = sum(datos)
media = suma / num

suma_cuadrados = sum([(x - media) ** 2 for x in datos])
desviacion_tipica = (suma_cuadrados / num) ** 0.5

print(f"Media: {media}")
print(f"Desviación típica: {desviacion_tipica}")