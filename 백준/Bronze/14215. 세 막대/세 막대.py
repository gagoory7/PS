import sys

num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()

if num_list[2] >= num_list[1] + num_list[0]:
    num_list[2] = num_list[1] + num_list[0] - 1
    print(sum(num_list))
else: 
    print(sum(num_list))