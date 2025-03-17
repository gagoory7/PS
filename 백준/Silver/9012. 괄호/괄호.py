N = int(input())

for _ in range(N) :
    stack = []
    s = input()
    for _ in s :
        if _ == '(' :
            stack.append(_)
        elif _ == ')' :
            if stack :
                stack.pop()
            else :
                print('NO')
                break
    else :
        if not stack :
            print('YES')
        else :
            print('NO')