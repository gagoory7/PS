

n, m = map(int,input().split())

set1 = set()

for i in range(n):
    set1.add(input())

data =[]

for _ in range(m):
    data.append(input())

count = 0

for i in range(m):
    if data[i] in set1:
        count+=1

print(count)