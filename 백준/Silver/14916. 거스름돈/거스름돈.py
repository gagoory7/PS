n = int(input())

c = 0

while n != 0 :
    if n == 1 or n ==3 :
        c = -1 
        break
    c += n//5
    n = n % 5
    if n % 2 == 0 :
        pass
    else :
        n += 5
        c -= 1
    c += n//2
    n = n % 2

print(c)