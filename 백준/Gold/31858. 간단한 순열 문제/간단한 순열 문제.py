from collections import deque

n = int(input())
p = list(map(int,input().split()))


stack = deque()

count = 0

for x in p :
    while stack and stack[-1] < x :
        stack.pop()
        count +=1

    if not stack :
        stack.append(x)
        continue

    stack.append(x)
    count +=1    

print(count)