#1181

data = []

for i in range(int(input())):
    data.append(input())

data = set(data)
data = list(data)
data.sort(key = lambda x : (len(x),x))

for _ in data:
    print(_)