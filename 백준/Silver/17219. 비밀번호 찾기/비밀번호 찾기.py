import sys

input = sys.stdin.readline

n,m = map(int,input().split())

pass_dict = {}

for _ in range(n) :
    s = input().split()
    pass_dict[s[0]] = s[1]


for _ in range(m):
    s = input().strip()
    print(pass_dict[s])