import sys

inut = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())

    clothes = {}
    for _ in range(n) :
        a,b = input().split()
        if b in clothes :
            clothes[b] += 1
        else :
            clothes[b] = 1

    counts = list(clothes.values())

    c = 1
    for count in counts :
        c *= (count+1)

    print(c-1)