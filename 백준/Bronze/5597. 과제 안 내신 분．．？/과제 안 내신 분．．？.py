a = []
for i in range(28) :
  a.append(int(input()))

b = list(range(31))
b.pop(0)


for i in range(30):
  if b[i] not in a :
    print(b[i])