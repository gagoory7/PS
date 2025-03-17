from collections import deque

N = int(input())
num_list = deque(enumerate(map(int,input().split(' '))))
ans = []

while num_list :
    
    idx,paper = num_list.popleft()
    ans.append(str(idx+1))

    if paper > 0 :
        num_list.rotate(-(paper-1))
    elif paper < 0 :
        num_list.rotate(-paper)


print(' '.join(ans))