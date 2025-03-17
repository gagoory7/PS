def fac(x) :
    mul = 1
    for i in range(1,x+1) :
        mul *= i

    return mul

m,n  = map(int,input().split())

print(int(fac(m) / fac(n) / fac(m-n)))