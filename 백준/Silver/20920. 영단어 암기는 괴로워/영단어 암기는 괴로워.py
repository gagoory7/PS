import sys

n, m = map(int, sys.stdin.readline().split())

str_dic = {}

for _ in range(n):
    tmp = sys.stdin.readline().strip()  
    if len(tmp) >= m:  
        if tmp in str_dic:
            str_dic[tmp] += 1
        else:
            str_dic[tmp] = 1

sorted_dict = sorted(
    str_dic.items(),
    key=lambda item: (-item[1], -len(item[0]), item[0])
)


for i, _ in sorted_dict:
    print(i)