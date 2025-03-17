n = int(input())

num_list = [0] * 1001

num_list[1] = 1
num_list[2] = 2

for i in range(3,1000+1) :
    num_list[i] = (num_list[i-1] + num_list[i-2]) % 10007

print(num_list[n])