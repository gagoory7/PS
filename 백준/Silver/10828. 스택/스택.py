import sys
input=sys.stdin.readline
n = int(input())
num_list = []

for _ in range(n) :
    s = input().split()
    if s[0] == 'push' :
        num_list.append(s[1])
    elif s[0] == 'pop' :
        if num_list :
            print(num_list.pop(-1))
        else :
            print(-1)
    elif s[0] == 'size' :
        print(len(num_list))
    elif s[0] =='empty' : 
        if num_list :
            print(0)
        else :
            print(1)
    elif s[0] == 'top' :
        if num_list :
            print(num_list[-1])
        else :
            print(-1)
