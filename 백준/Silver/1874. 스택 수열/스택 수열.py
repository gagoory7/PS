n = int(input())

stack = []
target = []
count = 1

for i in range(1,n+1) :
    num = int(input())

    while count <= num :
        stack.append(count)
        target.append('+')
        count +=1
    
    if stack[-1] == num :
        stack.pop()
        target.append('-')
    
    else :
        break

if len(stack) != 0 :
    print('NO')
else :
    for i in target :
        print(i)