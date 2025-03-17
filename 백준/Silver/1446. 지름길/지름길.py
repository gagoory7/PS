N, target = map(int,input().split())

dis_list = []

for i in range(N):
    x = list(map(int, input().split()))  
    dis_list.append(x)

dis_list.sort(key = lambda x : (x[0],x[1],x[2]))

num_list = [i for i in range(target+1) ]

for x in dis_list :
    q,w,e = x
    if w <= target :
        num_list[w] = min(num_list[q]+e,num_list[w])
        for idx, value in enumerate(range(w, target + 1)):
            
            num_list[idx+w] = min(num_list[w] + idx, num_list[w+idx])

print(num_list[target])   