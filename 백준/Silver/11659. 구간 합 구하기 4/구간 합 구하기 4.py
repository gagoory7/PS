import sys

input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int,input().split()))
total = [0]
tmp = 0

for i in nums :
    tmp = tmp + i
    total.append(tmp)

for _ in range(m) :
    a, b = map(int,input().split())
    print(total[b] - total[a-1])    
    