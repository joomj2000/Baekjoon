import sys

sys.setrecursionlimit(1000000)

maps=[]
for i in range(9):
    maps.append(list(map(int,sys.stdin.readline().strip())))

# 유효성 검사 배열
rows = [[False] * 10 for _ in range(9)]
cols = [[False] * 10 for _ in range(9)]
squares = [[False] * 10 for _ in range(9)]

to_fill = []

# 초기 상태 설정
for i in range(9):
    for j in range(9):
        num = maps[i][j]
        if num == 0:
            to_fill.append((i, j))
        else:
            rows[i][num] = True
            cols[j][num] = True
            squares[(i // 3) * 3 + (j // 3)][num] = True

def backtracking(k):
    if k == len(to_fill):
        for row in maps:
            print("".join(map(str, row)))
        sys.exit()

    i, j = to_fill[k]
    square_index = (i // 3) * 3 + (j // 3)

    for num in range(1, 10):
        if not rows[i][num] and not cols[j][num] and not squares[square_index][num]:
            maps[i][j] = num
            rows[i][num] = cols[j][num] = squares[square_index][num] = True

            backtracking(k + 1)

            maps[i][j] = 0
            rows[i][num] = cols[j][num] = squares[square_index][num] = False

backtracking(0)
