import math

def solve():
    n, x1_sprinkler, y1_sprinkler, x2_sprinkler, y2_sprinkler = map(int, input().split())
    flowers = []
    for _ in range(n):
        flowers.append(list(map(int, input().split())))

    min_r_squared_sum = float('inf')

    # Calculate squared distances
    dist1_sq = []
    dist2_sq = []
    for fx, fy in flowers:
        dist1_sq.append((fx - x1_sprinkler)**2 + (fy - y1_sprinkler)**2)
        dist2_sq.append((fx - x2_sprinkler)**2 + (fy - y2_sprinkler)**2)

    r1_sq = max(dist1_sq)
    min_r_squared_sum = min(min_r_squared_sum, r1_sq)

    r2_sq = max(dist2_sq)
    min_r_squared_sum = min(min_r_squared_sum, r2_sq)

    for i in range(n):
        r1_squared = dist1_sq[i]
        r2_squared = 0
        for j in range(n):
            if dist1_sq[j] > r1_squared:
                r2_squared = max(r2_squared, dist2_sq[j])
        min_r_squared_sum = min(min_r_squared_sum, r1_squared + r2_squared)

    # Iterate through possible r2^2 values based on distances to sprinkler 2
    for i in range(n):
        r2_squared = dist2_sq[i]
        r1_squared = 0
        for j in range(n):
            if dist2_sq[j] > r2_squared:
                r1_squared = max(r1_squared, dist1_sq[j])
        min_r_squared_sum = min(min_r_squared_sum, r1_squared + r2_squared)

    print(min_r_squared_sum)

solve()