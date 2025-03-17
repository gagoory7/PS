N = int(input())

str_dict = {}

for _ in range(N) :
    str1 = input().split('.')
    ex = str1[1]
    if ex in str_dict.keys() :
        str_dict[ex] +=1
    else :
        str_dict[ex] = 1

sorted_dict = sorted(str_dict.items(), key = lambda item : (item[0]) )

for k,v in sorted_dict :
    print(k+' '+str(v))