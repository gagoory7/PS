# 9506

while True :
    m = int(input())
    if m == -1 :
        break

    i = 1
    num_list = []
    while i < m :
        if m % i == 0 :
            num_list.append(i)
        i+=1
    
    if sum(num_list) == m :
        print(str(m) +' = ',end ='')
        for i in num_list:
            if i == num_list[len(num_list)-1]:
                print(i)
            else :
                print(i , end = ' + ')
            
    else :
        print(str(m), 'is NOT perfect.')