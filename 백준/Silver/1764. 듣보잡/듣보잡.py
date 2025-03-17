n,m = map(int,input().split())
set1 = set()
set2 = set()

for _ in range(n):
    set1.add(input())
for _ in range(m):
    set2.add(input())

list1 = list(set1 & set2)
list1.sort()
print(len(list1))

for _ in range(len(list1)):
    print(list1[_])