#18870

n = int(input())

data = list(map(int,input().split()))

d_data = set(data)
d_data = list(d_data)
d_data.sort()

dic = {d_data[i] : i for i in range(len(d_data))}
for i in range(n):
    print(dic[data[i]],end=' ')