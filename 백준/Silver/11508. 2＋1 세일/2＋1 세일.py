n = int(input())

price = [int(input()) for _ in range(n)]

price.sort(reverse=True)

result = 0
for i in range(2,len(price),3) :
    result += price[i]

print(sum(price)-result)