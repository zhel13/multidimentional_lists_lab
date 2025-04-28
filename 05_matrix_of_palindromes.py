row, col = [int(x) for x in input().split()]

# matrix = []

for i in range(row):
    # matrix.append([])
    for j in range(col):
        print(chr(97+i)+chr(97+i+j)+chr(97+i), end=" ")
    print()
        # matrix[i].append(result)

# [print(*i) for i in matrix]

