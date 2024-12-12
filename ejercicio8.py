palabra = input("Escribe una palabra: ")
palabrainversa = palabra
palabra = list(palabra)
palabrainversa = list(palabrainversa)
palabrainversa.reverse()
if palabra == palabrainversa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")