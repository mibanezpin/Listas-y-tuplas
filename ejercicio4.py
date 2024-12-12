premio = []
for i in range(6):
    premio.append(int(input("Escribe el número ganador: ")))
premio.sort()
print("Los números ganadores son " + str(premio))