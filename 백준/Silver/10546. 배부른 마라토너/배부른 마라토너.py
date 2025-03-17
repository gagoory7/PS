import sys
input = sys.stdin.readline

n = int(input())

name_dict = {}

for _ in range(n*2-1) :
    name = input()

    if name in name_dict.keys() :
        name_dict[name] +=1
    else :
        name_dict[name] = 1

ans = [ k for k,v in name_dict.items() if v % 2 == 1]

print(ans[0])