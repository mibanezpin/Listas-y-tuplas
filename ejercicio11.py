A = ((1, 2, 3),
     (4, 5, 6))
B = ((-1, 0),
     (0, 1),
     (1, 1))
resultado = [[0,0],
          [0,0],
          [0,0]]
for i in range (len(A)):  

    for j in range(len(A[0])):
        resultado [i][j] = A[i][j] + B[i][j] 
for r in resultado:
    print(r)
          