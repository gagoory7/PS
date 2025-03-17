# 1929

n,m = map(int,input().split())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True
    
for i in range(n,m+1):
    if i == 1:
        continue
    if check(i):
        print(i)