number = int(input())

matrix = [[int(el)for el in input().split(", ")]for _ in range(number)]

primary = [matrix[i][i] for i in range(number)]
secondary = [matrix[i][number - i - 1] for i in range(number)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")

