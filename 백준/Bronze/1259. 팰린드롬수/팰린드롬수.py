while True:
    num_list = input()
    if num_list == '0' :
        break
    
    num_list = list(num_list)
    
    length = len(num_list)
    count = 0

    for i in range(0,length//2) :
        if num_list[i] == num_list[length-i-1]:
            continue
        else :
            count = 1
            break
    if count == 0 :
        print('yes')
    else :
        print('no')