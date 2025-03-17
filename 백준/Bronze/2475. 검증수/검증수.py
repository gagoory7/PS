n = list(map(int,input().split()))

num = 0
for x in n :
    num += x**2
   
print(num%10)