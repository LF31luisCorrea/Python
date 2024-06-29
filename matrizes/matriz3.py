matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = int(input("Digite numeros para a matriz: "))

print(matrix)

for i in range(0, 3):
    print(matrix[i])