a = input()

n = len(a)

cnt = 0
c = n-1
for i in range(n):

  if a[i] != a[c-i]:
    cnt +=1

if cnt == 0:
  print('1')
else :
  print('0')  