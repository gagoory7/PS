n = int(input())

price = list(map(int,input().split()))

num_list = [ 0 for _ in range(n+1)]


for i in range(1,n+1) :
    for j in range(1,i+1) :
        num_list[i] = max(num_list[i], num_list[i-j]+ price[j-1])

print(num_list[n])