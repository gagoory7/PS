import sys

input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))

# 초기 윈도우 합 계산
current_sum = sum(nums[:x])
max_sum = current_sum
count = 1

# 슬라이딩 윈도우 적용
for i in range(x, n):
    current_sum += nums[i] - nums[i - x]  # 윈도우 이동
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)
