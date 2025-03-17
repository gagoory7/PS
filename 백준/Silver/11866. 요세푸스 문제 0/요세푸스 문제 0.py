from collections import deque

a, b = map(int,input().split())

num_list = list(range(1,a+1))

idx = 0
dic = []

while num_list :
    idx += b-1
    if idx >= len(num_list):
        idx %= len(num_list)
    dic.append(str(num_list.pop(idx)))

print("<", ", ".join(dic), ">",sep='')