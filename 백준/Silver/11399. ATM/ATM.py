import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split())) 

nums.sort(reverse=True)
c = 0
for i in range(n) :
    for j in range(i,n) :
        c += nums[j]

print(c)