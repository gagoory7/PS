import sys

input = sys.stdin.readline

def solve():
    n, x1, y1, x2, y2 = map(int, input().split())
    flowers = [list(map(int, input().split())) for _ in range(n)]

    d1 = [((fx - x1)**2 + (fy - y1)**2) for fx, fy in flowers]
    d2 = [((fx - x2)**2 + (fy - y2)**2) for fx, fy in flowers]

    ans = float('inf')
    if n > 0:
        ans = min(max(d1), max(d2))

    for i in range(n):
        r1_sq = d1[i]
        r2_sq_needed = max((d2[j] for j in range(n) if d1[j] > r1_sq), default=0)
        ans = min(ans, r1_sq + r2_sq_needed)

        r2_sq = d2[i]
        r1_sq_needed = max((d1[j] for j in range(n) if d2[j] > r2_sq), default=0)
        ans = min(ans, r1_sq_needed + r2_sq)

    print(ans)

solve()