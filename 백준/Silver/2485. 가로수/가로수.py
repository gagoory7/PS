# 2485
def gcd(a,b):
    while b> 0 :
        a,b = b,a%b
    return a
    
n = int(input())
a1 = int(input())
list1 = []

for _ in range(n-1):
    num = int(input())
    list1.append(num-a1)
    a1 = num
g = list1[0]

for j in range(1,len(list1)) :
    g = gcd(g,list1[j])

result = 0

for a in list1:
    result += a//g -1
    

print(result)