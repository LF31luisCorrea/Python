#Matriz centralizada e espacada, escrita final corretamente
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = int(input(f"Digite numeros para a matriz[{i}, {j}]: "))

print("-=" * 30)

for i in range(0, 3):
    for j in range(0,3):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()