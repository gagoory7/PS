import sys

input = sys.stdin.readline

n = int(input()) 

talls  = [int(input()) for _ in range(n)]

stack = []

count = 0

for tall in talls :
    while stack and stack[-1][0] < tall :
        count += stack.pop()[1]

    if not stack :
        stack.append((tall,1))
        continue

    if stack[-1][0] == tall :
        c = stack.pop()[1]
        count += c
        if stack :
            count +=1
        stack.append( (tall, c+1))
    
    else :
        stack.append( (tall,1))
        count +=1    

print(count)