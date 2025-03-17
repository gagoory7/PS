m = int(input())
dic1 = {}

list1 = list(map(int,input().split()))

for _ in range(m):
    if list1[_] in dic1.keys():
        dic1[list1[_]] +=1
    else :
        dic1[list1[_]] =1

n = int(input())

list2 = list(map(int,input().split()))

for _ in range(n):
    if list2[_] in dic1.keys():
        print(dic1[list2[_]],end=' ')
    else:
        print(0,end = ' ')