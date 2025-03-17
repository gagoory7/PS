# 2501

m,n = map(int,input().split())
i=1
num_list = []
while i <= m : 
    if m%i ==0:
        num_list.append(i)
    i+=1

if len(num_list) < n:
    print(0)
else :
    print(num_list[n-1])