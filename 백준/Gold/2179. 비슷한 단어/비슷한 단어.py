n = int(input())

a = [ input() for _ in range(n) ] 

b = sorted(list(enumerate(a)),key = lambda x: x[1])

def check(a,b) :
    count = 0 
    for i in range(min(len(a),len(b))) : 
        if a[i] == b[i] :
            count +=1
        else :
            break

    return count


length = [0] * (n+1)
maxlength = 0
for i in range(n-1) :
    tmp = check(b[i][1],b[i+1][1])
    maxlength = max(tmp,maxlength)
    length[b[i][0]] = max(tmp,length[b[i][0]])
    length[b[i+1][0]] = max(tmp,length[b[i+1][0]])

first = 0

for i in range(n) : 
    if first == 0 :
        if length[i] == max(length) :
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else :
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break