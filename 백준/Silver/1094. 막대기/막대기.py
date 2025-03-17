x = int(input())

sticks = [64,32,16,8,4,2,1]
count = 0

for cm in sticks : 
    if x >= cm:
        count += 1
        x -= cm
        
    if x == 0:
        break


print(count)