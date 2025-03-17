while True :
    
    s = input()
    if s=='.' :
        break

    s_list = list(s)
    
    stack = []

    for _ in s_list :
        if _ == '(' :
            stack.append(_)
            
        elif _ == ')' :
            if stack :
                if stack[-1] == '(':
                    stack.pop()
                else :
                    print('no')
                    break
            else :
                print('no')
                break

        elif _ == '[' :
            stack.append(_)
            
        elif _ == ']' :
            if stack :
                if stack[-1] == '[':
                    stack.pop()
                else :
                    print('no')
                    break
            else :
                print('no')
                break

        elif _ =='.' :
            if not stack :
                print('yes')
            else :
                print('no')
            