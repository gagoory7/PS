import sys
input = sys.stdin.readline

def solve():
    n, x1, y1, x2, y2 = map(int, input().split())
    flowers = [tuple(map(int, input().split())) for _ in range(n)]

    d1 = [(fx - x1) ** 2 + (fy - y1) ** 2 for fx, fy in flowers]
    d2 = [(fx - x2) ** 2 + (fy - y2) ** 2 for fx, fy in flowers]

    ans = float('inf')

    for i in range(n + 1):  # i는 r1^2의 후보
        r1_sq = 0 if i == n else d1[i]
        r2_sq = max((d2[j] for j in range(n) if d1[j] > r1_sq), default=0)
        ans = min(ans, r1_sq + r2_sq)

    print(ans)

solve()
