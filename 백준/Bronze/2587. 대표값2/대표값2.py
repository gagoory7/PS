num_list = []
for i in range(5) :
    num_list.append(int(input()))

num_list.sort()
print( int(sum(num_list)/len(num_list)))
print( num_list[2])