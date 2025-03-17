n,m =  map(int,input().split())

s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n:
    s+= str(arr[n%m])
    n//=m

print(s[::-1])