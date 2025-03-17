import sys

input = sys.stdin.readline

s = input()

ts = 0
str_list = []

for i in range(len(s)) :
    x = s[i]
    if x.isdigit() :
        ts = ts * 10 + int(x)
    else :
        str_list.append(int(ts))
        str_list.append(x)
        ts = 0
    
    if i == len(s) - 1 :
        str_list.append(int(ts))

count = 0 

plus = True
for i in range(len(str_list)) :
    if plus :
        if isinstance(str_list[i], int) :
            count += str_list[i]
        elif str_list[i] == '-' :
            plus = False
        else :
            pass
    else :
        if isinstance(str_list[i], int) :
            count -= str_list[i]
    
print(count)