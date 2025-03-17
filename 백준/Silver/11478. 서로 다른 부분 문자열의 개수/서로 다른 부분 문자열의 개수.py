# 11478

a = input()
set1 = set()

for i in range(len(a)):
    b = len(a)-i
    for j in range(b):
        set1.add(a[j:j+i+1])

print(len(set1))