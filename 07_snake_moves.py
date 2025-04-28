from collections import deque

r, c = [int(n) for n in input().split()]
text = deque(input())
matrix = []

for row in range(r):
    matrix.append(['']*c)
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = text[0]
        else:
            matrix[row][-1-col] = text[0]
        text.rotate(-1)
[print(''.join(j)) for j in matrix]
































# result = deque(text)
#
# for row in range(r):
#     while len(result) < c:
#         result.extend(text)
#     if row % 2 == 0:
#         print(*[result.popleft() for _ in range(c)], sep="")
#     else:
#         print(*[result.popleft() for _ in range(c)][::-1], sep="")
# matrix = []
# for row in range(r):
#     matrix.append(['']*c)
#     for col in range(c):
#         if row % 2 == 0:
#             matrix[row][col] = text[0]
#         else:
#             matrix[row][-1-col] = text[0]
#         text.rotate(-1)
# [print("".join(matrix[x])) for x in range(r)]