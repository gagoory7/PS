#1515

n = input()
ans =0

while True :
    ans +=1
    t = str(ans)
    while len(t) > 0 and len(n) > 0 :
        if t[0] == n[0] :
            n = n[1:]
        t = t[1:]
    if n == '' :
        print(ans)
        break