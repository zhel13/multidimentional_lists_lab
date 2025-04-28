def check_p_position():
    for r in range(rows):
        for c in range(cols):
            if "P" in matrix[r]:
                return r, matrix[r].index("P")


def check_valid_index(row, col, player=False):
    global player_location
    global has_won
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        has_won = True


def bunnies_position():
    positions = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "B":
                positions.append([r, c])
    return positions


def bunnies_movement(bun_pos):
    for row, col in bun_pos:
        for v in directions.values():
            new_row = row + v[0]
            new_col = col + v[1]

            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = "B"


def game_result(status="won"):
    [print(*matrix[i], sep="") for i in range(rows)]
    print(f"{status}: {pl_row} {pl_col}")
    raise SystemExit


def is_alive(row, col):
    if matrix[row][col] == "B":
        game_result("dead")


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]

commands = input()
has_won = False
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

pl_row, pl_col = check_p_position()
matrix[pl_row][pl_col] = "."
player_location = [pl_row, pl_col]

for command in commands:
    new_pl_row = pl_row + directions[command][0]
    new_pl_col = pl_col + directions[command][1]

    if check_valid_index(new_pl_row, new_pl_col, True):
        pl_row, pl_col = new_pl_row, new_pl_col
    bunnies_movement(bunnies_position())

    if has_won:
        game_result()
    is_alive(pl_row, pl_col)


