import sys

input = sys.stdin.readline

target = input().strip()
boom = input().strip()

stack = []

boom_len = len(boom)

for char in target:
    stack.append(char)
    if len(stack) >= boom_len and ''.join(stack[-boom_len:]) == boom:
        del stack[-boom_len:]

if stack :
    result = ''.join(stack)
    print(result)
else :
    print('FRULA')