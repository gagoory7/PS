import sys

input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int,input().split()))

start, end = 0, max(nums)

while start <= end :
    mid = (start + end) // 2
    log = 0
    for i in nums :
        if i > mid :
            log += i - mid
    if log < m :
        end = mid -1
    else :
        start = mid + 1

print(end)