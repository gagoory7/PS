import sys

input = sys.stdin.readline

n = int(input())

used_col = [False] * n
used_dig1 = [False] * (2*n) # \
used_dig2 = [False] * (2*n) # /

count = 0

def backtracking(row) :
    global count
    if row == n :
        count +=1
        return
    
    for col in range(n) :
        if not used_col[col] and not used_dig1[row-col + n] and not used_dig2[ row+ col] :
            used_col[col] = True
            used_dig1[row-col+n] = True
            used_dig2[row+col] = True
            backtracking(row+1)
            used_col[col] = False
            used_dig1[row-col+n] = False
            used_dig2[row+col] = False


backtracking(0)
print(count)