from collections import deque

number = int(input())
commands = deque(input().split())


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = [[i for i in input().split()] for _ in range(number)]
miner_pos = []
total_coal = 0
current_coal = 0

for row in range(len(matrix)):
    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index('s')]
        matrix[row][miner_pos[1]] = "*"
    total_coal += matrix[row].count('c')

for command in commands:
    r = directions[command][0] + miner_pos[0]
    c = directions[command][1] + miner_pos[1]

    if not (0 <= r < number and 0 <= c < number):
        continue
    miner_pos = [r, c]

    if matrix[r][c] == "c":
        current_coal += 1
        if current_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"

else:
    print(f"{total_coal - current_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")



