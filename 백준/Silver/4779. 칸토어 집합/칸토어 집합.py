import sys

input = sys.stdin.readline

def solve(n) :
    if n == 1 :
        return "-"
    else :
        left = solve(n//3)
        center = " " * (n//3)
        return left + center + left

while True :
    try :
        n = int(input())
        rst = solve(3**n)
        print(rst)
    except :
        break