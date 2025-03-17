n = input()
num_list = []
for i in range(len(n)) :
    num_list.append(int(n[i]))
num_list.sort(reverse=True)

for i in num_list:
    print(i,end='')