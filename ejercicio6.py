Asignaturas = ["Física", "Lengua", "Matemáticas", "Química", "Historia", "Geología"]
aprobadas = []
for asignatura in Asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if nota >= 5:
        aprobadas.append(asignatura)
for asignatura in aprobadas:
    Asignaturas.remove(asignatura)
print("Tienes que volver a hacer" + str(Asignaturas))