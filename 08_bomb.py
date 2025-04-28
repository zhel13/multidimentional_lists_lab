def valid_index(r, c):
    if 0 <= r < num and 0 <= c < num:
        if matrix[r][c] > 0:
            return True


num = int(input())
matrix = [[int(x) for x in input().split(" ")] for i in range(num)]
indices = input().split()
bomb_positions = []
active_cells = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up-left": (-1, -1),
    "up-right": (-1, 1),
    "down-left": (1, -1),
    "down-right": (1, 1),
}

for i in range(len(indices)):
    bomb_index = [int(x) for x in indices[i].split(',')]
    bomb_positions.append(bomb_index)

for i in range(len(bomb_positions)):
    for direction in directions:
        new_row = bomb_positions[i][0] + directions[direction][0]
        new_col = bomb_positions[i][1] + directions[direction][1]
        index_check = [new_row, new_col]
        if valid_index(new_row, new_col):
            matrix[new_row][new_col] -= matrix[bomb_positions[i][0]][bomb_positions[i][1]]
    matrix[bomb_positions[i][0]][bomb_positions[i][1]] = 0

counter = 0
for col in matrix:
    for i in col:
        if i > 0:
            counter += 1
            active_cells.append(i)

print(f"Alive cells: {counter}")
print(f"Sum: {sum(active_cells)}")
[print(*r) for r in matrix]
