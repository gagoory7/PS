import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graphs = [ list(map(int,input().split())) for _ in range(n) ]

chicken = []
home = []
for i in range(n) :
    for j in range(n) :
        if graphs[i][j] == 2 :
            chicken.append((i,j))
        if graphs[i][j] == 1 :
            home.append((i,j))  
results = []

def comb(x,result,target) :
    if len(result) == target:
        results.append(result[:])
        return
    for i in range(x,len(chicken)) :

        comb(i+1,result+[i],target)

comb(0,[],m)

answer = 1000000

for chi in results: 
    temp = 0           
    for h in home: 
        chi_len = 999   
        for j in chi:
            chi_len = min(chi_len, abs(h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1]))
        temp += chi_len
    answer = min(answer, temp)

print(answer)