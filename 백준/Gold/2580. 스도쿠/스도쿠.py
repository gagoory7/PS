import sys
input = sys.stdin.readline

blank = []
graphs = [ list(map(int,input().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if graphs[i][j] == 0:
            blank.append([i, j])  # i: row, j: col

def check_row(row, x):
    for i in range(9):
        if graphs[row][i] == x:
            return False
    return True

def check_col(col, x):
    for i in range(9):
        if graphs[i][col] == x:
            return False
    return True

def check_sq(row, col, x):
    for i in range(3):
        for j in range(3):
            if graphs[(row//3)*3 + i][(col//3)*3 + j] == x:
                return False
    return True

def backtracking(depth):
    if depth == len(blank):
        for graph in graphs:
            print(*graph)
        exit()  # 정답 하나만 출력하고 종료
        return
    
    row, col = blank[depth]

    for i in range(1, 10):
        if check_row(row, i) and check_col(col, i) and check_sq(row, col, i):
            graphs[row][col] = i
            backtracking(depth + 1)
            graphs[row][col] = 0

backtracking(0)
