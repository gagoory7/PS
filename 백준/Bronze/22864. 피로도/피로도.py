a,b,c,m = map(int,input().split())
q = 0
total = 0
for i in range(24) :
        if q + a <= m :
            q +=a
            total += b
        else :
            if q-c >= 0 :
                q -=c
            else :
                q = 0 
                
print(total)