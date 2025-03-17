import sys

input = sys.stdin.readline


n , k = map(int,input().split())

prices = [ int(input()) for _ in range(n)]

prices.sort(reverse=True)
count = 0
while k != 0 :
    for price in prices :
        if k >= price :
            count += k // price
            k = k % price

print(count)
    