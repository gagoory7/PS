A = list(map(int,input().split()))
B = list(map(int,input().split()))

a_s ,b_s = 0, 0

last = 0 

for i in range(len(A)) :
    a = A[i]
    b = B[i]

    if a> b : 
        a_s +=3
        last = 'a'
    elif a == b :
        a_s +=1
        b_s +=1
    else :
        b_s +=3
        last = 'b'

print(a_s,b_s)
if a_s > b_s : 
    print('A')
elif a_s == b_s :
    if last == 'a' : 
        print('A')
    elif last == 'b' :
        print('B')
    else : 
        print('D')
else : 
    print('B')