row, col = [int(x) for x in input().split()]
matrix = []
for r in range(row):
    matrix.append(input().split())


def check_indices(args):
    return {args[0], args[2]}.issubset(range(row)) and {args[1], args[3]}.issubset(range(col))


def check_valid(com, ind):
    if com == "swap" and len(ind) == 4 and check_indices(ind):
        row1, col1, row2, col2 = ind
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*matrix[i]) for i in range(row)]

    else:
        print("Invalid input!")


while True:
    command, *indices = [int(x) if x.isdigit() else x for x in input().split()]
    if command == "END":
        break
    else:
        check_valid(command, indices)






















# def indices_check(indices):
#     return {indices[0], indices[2]}.issubset(range(row)) and {indices[1], indices[3]}.issubset(range(col))
#
#
# def check_command(command_data, indices):
#     if len(indices) == 4 and command_data == "swap" and indices_check(indices):
#         row1, col1, row2, col2 = indices
#         data[row1][col1], data[row2][col2] = data[row2][col2], data[row1][col1]
#
#         [print(*el) for el in data]
#     else:
#         print("Invalid input!")
#
#
# while True:
#     command, *args = [int(x) if x.isdigit() else x for x in input().split()]
#     if command == "END":
#         break
#     else:
#         check_command(command, args)
