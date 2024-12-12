Palabra = input("Escribe una palabra: ")
Vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in Vocales: 
    tiempo = 0
    for letra in Palabra: 
        if letra == vocal:
            tiempo += 1
    print("La vocal " + vocal + " aparece " + str(tiempo) + " veces")