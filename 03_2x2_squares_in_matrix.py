row, col = [int(x) for x in input().split()]

matrix = [[el for el in input().split()] for _ in range(row)]
blocks = 0

for i in range(row - 1):
    for j in range(col - 1):
        symbol = matrix[i][j]

        if symbol == matrix[i + 1][j] and symbol == matrix[i][j + 1] and symbol == matrix[i + 1][j + 1]:
            blocks += 1

print(blocks)