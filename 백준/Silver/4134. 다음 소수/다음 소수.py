n = int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True


for i in range(n):
    a = int(input())
    while True :
        if a ==0 or a ==1 :
            print(2)
            break
        if check(a):
            print(a)
            break
        else:
            a+=1