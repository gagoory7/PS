n,m = map(int,input().split())
know_list = set(input().split()[1:])

party_list = []

for i in range(m):
    party_list.append(set(input().split()[1:]))

total = 0 
for i in range(m) :
    for party in party_list :
        if party & know_list :
            know_list = know_list.union(party)
    

for party in party_list:
    if party & know_list :
        continue
    total +=1

print(total)