from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ss = input().strip()

stack = deque()
remove = k

for digit in ss:
    d = int(digit)
    while remove > 0 and stack and stack[-1] < d:
        stack.pop()
        remove -= 1
    stack.append(d)

# k개를 다 안 뺐으면 뒤에서 자르기
while remove > 0:
    stack.pop()
    remove -= 1

print(''.join(str(x) for x in stack))