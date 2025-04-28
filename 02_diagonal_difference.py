number = int(input())

matrix = [[int(el)for el in input().split()]for _ in range(number)]

primary = [matrix[i][i] for i in range(number)]
secondary = [matrix[i][number - i - 1] for i in range(number)]
result = abs(sum(primary)-sum(secondary))

print(result)


