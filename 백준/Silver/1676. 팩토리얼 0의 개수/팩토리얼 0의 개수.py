n = int(input())

num2, num5 = 0, 0 

for i in range(2,n+1) :
    num = i 
    if num % 2 == 0 :
        while num % 2 == 0 :
            num2 +=1
            num  = num / 2
    if num % 5 == 0 :
        while num % 5 == 0 :
            num5 +=1
            num = num /5

count = min(num2,num5)

print(count) 