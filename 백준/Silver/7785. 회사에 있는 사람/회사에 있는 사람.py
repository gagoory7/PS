# 7785

n = int(input())

set1 = set()

for i in range(n):
    m,n = input().split()
    if n == 'enter':
        set1.add(m)
    else:
        set1.remove(m)

for _ in sorted(list(set1),reverse=True) :
    print(_)