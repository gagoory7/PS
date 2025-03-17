N = int(input())

num_list = list(map(int, input().split()))
target = 1 
stack = []


for i in num_list :
    stack.append(i)
    while stack and stack[-1] == target :
        stack.pop()
        target +=1

if len(stack) == 0 :
    print('Nice')
else:
    print('Sad')