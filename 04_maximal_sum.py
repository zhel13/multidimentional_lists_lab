row, col = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(row)]

max_sum = float("-inf")
matrix_result = []

for i in range(row - 2):
    for j in range(col - 2):

        firs_row = matrix[i][j:j+3]
        second_row = matrix[i+1][j:j+3]
        third_row = matrix[i+2][j:j+3]

        current_sum = sum(firs_row) + sum(second_row) + sum(third_row)

        if max_sum < current_sum:
            max_sum = current_sum
            matrix_result = [firs_row, second_row, third_row]
print(f"Sum = {max_sum}")
[print(*i) for i in matrix_result]
