n =int(input())
target = int(input())
num_list =  [int(input()) for _ in range(n-1)]
count = 0

if n == 1 :
    pass
else :
    while target <= max(num_list) :
        target +=1
        count +=1
        num_list[num_list.index(max(num_list))] -= 1

print(count)