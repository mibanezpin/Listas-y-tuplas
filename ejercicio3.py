Asignaturas = ["Matematicas", "Quimica", "Fisica", "Historia", "Lengua", "Geología"]
notas = []
for asignatura in Asignaturas:
    nota = input("¿Qué nota he sacado en " + asignatura + "?")
    notas.append(nota)
for i in range(len(Asignaturas)):
    print("En " + Asignaturas[i] + " he conseguido sacar un " + notas[i])