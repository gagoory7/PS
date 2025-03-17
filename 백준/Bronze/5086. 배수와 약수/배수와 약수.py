# 5086
while True:
    m,n = map(int,input().split())
    if m ==0 & n==0 :
        break
    elif m % n ==0 :
        print('multiple')
    elif n%m ==0:
        print('factor')
    else :
        print('neither')