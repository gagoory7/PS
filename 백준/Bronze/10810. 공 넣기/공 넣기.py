a = input().split()
a = [int(x) for x in a]
m = a[0]
n = a[1]

basket = [0] *m

for i in range(n) :
  a = input().split()
  a = [int(x) for x in a]
  for j in range(a[0]-1,a[1]):
    basket[j] = a[2]

[print(x,end = ' ') for x in basket]
