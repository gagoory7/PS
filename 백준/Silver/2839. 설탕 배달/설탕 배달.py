# 2839

kg = int(input())

bag = 0

while kg>=0 :
    if kg % 5 == 0 :
        bag+= kg//5
        print(bag)
        break
    bag +=1
    kg -=3 
    if kg < 0:
        print(-1)