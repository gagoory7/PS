N = int(input())
a = input().split()
a = [int(x) for x in a ]
x = int(input())
count = 0

for i in range(N):
  if x == a[i]:
    count += 1

print(count)