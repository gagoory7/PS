n, k = map(int,input().split())

lengths = [int(input()) for _ in range(n)]

start = 1
end = max(lengths)

while start <= end :
    mid = (start + end) // 2
    lines = 0
    for i in lengths :
        lines += i // mid
    
    if lines >= k :
        start = mid + 1 
    else :
        end = mid - 1
    
print(end)