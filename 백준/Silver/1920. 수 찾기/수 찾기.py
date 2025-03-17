import sys
input = sys.stdin.readline

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(input().strip())
num_list = sorted(list(map(int, input().strip().split())))

m = int(input().strip())
target_list = list(map(int, input().strip().split()))

for target in target_list:
    print(binary_search(num_list,target))