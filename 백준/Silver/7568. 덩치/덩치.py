n = int(input())

sl = [ list(map(int,input().split())) for _ in range(n) ]


for i in sl : 
    rank = 1
    for j in sl :
        if i[0] < j[0] and i[1] < j[1] :
            rank +=1
    print(rank, end = " ")