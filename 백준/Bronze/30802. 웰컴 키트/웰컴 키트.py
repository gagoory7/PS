n = int(input())

num_list = list(map(int,input().split()))

T, P = map(int,input().split())

result = []

for num in num_list:
    quotient = num // T
    if num % T == 0:
        result.append(quotient)
    else:
        result.append(quotient + 1)


print(sum(result))

print( (n//P),(n%P))