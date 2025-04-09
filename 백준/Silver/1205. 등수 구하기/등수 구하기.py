n, k, p = map(int,input().split())

if n == 0 :
    print(1)
    
else :
    nums = list(map(int,input().split()))
    if n == p and nums[-1] >= k :
        print(-1)
    else :
        res = n +1
        for i in range(n) :
            if nums[i] <= k :
                res = i +1
                break
        print(res)