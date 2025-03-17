while True :
    test = input()
    if test == 'end' :
        break

    str_list = list(test)
    ans = 0

    if ('a' in str_list) or ('u' in str_list) or ('i' in str_list) or ('o' in str_list) or ('e' in str_list) :
        pass
    else : 
        ans = 1
        

    c1 = 0
    c2 = 0

    for x in str_list :
        if (x =='a') or (x=='e') or (x=='i') or (x=='o') or ( x=='u') :
            c2 = 0
            if c1 == 0 :
                c1 = 1
            else :
                c1 +=1
            
        else :
            c1 = 0
            if c2 == 0 :
                c2 = 1
            else :
                c2 +=1
        
        if ( c1 >= 3) or (c2 >= 3) :
            ans = 1
    
    count = 0
    for i in range(1,len(str_list)) :
        if (str_list[i] == 'e') or (str_list[i]=='o') :
            count = 0
            continue
        
        if str_list[i-1] == str_list[i] :
            count+=1
        else :
            count = 0
        
        if count >= 1 :
            ans = 1 
            pass

    if ans == 0 :
        print('<' + ''.join(str_list)+'> is acceptable.')
    else :
        print('<' + ''.join(str_list)+'> is not acceptable.')