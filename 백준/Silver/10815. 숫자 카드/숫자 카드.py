# 10815

n = int(input())
cards = set(map(int,input().split()))

m = int(input())
card = list(map(int,input().split()))

for _ in range(m) :
    i = 0
    if card[_] in cards :
        i=1
    print(str(i),end = ' ')