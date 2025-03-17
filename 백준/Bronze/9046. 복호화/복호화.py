import sys

n = int(sys.stdin.readline())

for _ in range(n):
    str_list = list(sys.stdin.readline().strip().replace(" ",""))
    str_dic = {}
    for i in str_list :
        if i in str_dic.keys() :
            str_dic[i] +=1
        else :
            str_dic[i] = 1
    
    max_value = max(str_dic.values())
    max_keys = [k for k,v in str_dic.items() if v == max_value]

    if len(max_keys) > 1 :
        print('?')
    else :
        print(max_keys[0])