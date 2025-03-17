from collections import Counter
import sys
input=sys.stdin.readline
n = int(input())

num_list = [ int(input()) for _ in range(n)]

num_list.sort()

cnt = Counter(num_list).most_common(2)



print(round(sum(num_list)/n))
print(num_list[int(n/2)])
if len(num_list) > 1 :
    if cnt[0][1] == cnt[1][1] :
        print(cnt[1][0])
    else :
        print(cnt[0][0])
else :
    print(cnt[0][0])
print(num_list[-1] - num_list[0])