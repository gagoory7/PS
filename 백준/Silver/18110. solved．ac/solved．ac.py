import math
import sys

def custom_round(value):
    return math.floor(value + 0.5)

input = sys.stdin.readline

n = int(input())

scores = []

                      
for _ in range(n) :
    scores.append(int(input()))

scores.sort()

index = custom_round(n*0.15)

if n == 0 :
    print(0)
else :
    if index == 0  :
        print(custom_round( sum(scores) / n))
    else :
        print(custom_round(sum(scores[index:-index])/(n-2*index)))