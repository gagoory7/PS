import sys

input = sys.stdin.readline

n, m = map(int, input().split())
scores = list(map(int, input().split())) 
scores.sort(reverse=True)  

score = 0
banker = 0

i = 0 
while i < m :
    i +=1
    if not scores :
        break
    a = scores.pop(0)
    if a < 0 :
        if scores :
            scores.pop()
    else :
        score += a
        if scores :
            scores.pop()


print(score)