import sys
input = sys.stdin.readline


N = int(input())

cost = [25,10,5,1]

for i in range(N):
    m = int(input())
    result = []
    for j in cost:
        result.append(m //j )
        m = m%j
    for k in result:
        print(k,end = ' ')