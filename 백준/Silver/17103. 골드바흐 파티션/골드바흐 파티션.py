# 17103

n = int(input())

m = 1000000+1
list1 = [1] *m
list1[0] = 0

for i in range(1, m):
    if i == 1:
        list1[i] = 0
    else:
        if list1[i] == 1:
            for j in range(2*i, m, i):
                list1[j] = 0
    
for _ in range(n):
    a = int(input())
    count = 0
    b = int(a/2)
    
    for i in range(1,b+1):

        if list1[i] ==1 and  list1[a-i]==1:
            count+=1
        
    print(count)