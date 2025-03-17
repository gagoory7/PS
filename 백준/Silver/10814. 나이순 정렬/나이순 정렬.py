# 10814

n = int(input())

data = []
for i in range(n):
    data.append( input().split())

data.sort(key = lambda x : int(x[0]))

for _ in data:
    print(_[0]+' '+_[1])