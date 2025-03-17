import sys

input = sys.stdin.readline

n = int(input())

sets  = set()

for _ in range(n) :
    s = input().split()
    type = s[0]
    
    if type == 'add' :
        sets.add(int(s[1]))
        
    elif type == 'remove' :
        sets.discard(int(s[1]))
        
    elif type == 'check' :
        if int(s[1]) in sets :
            print(1)
        else :
            print(0)
            
    elif type == 'toggle' :
        if int(s[1]) in sets :
            sets.discard(int(s[1]))
        else :
            sets.add(int(s[1]))
            
    elif type == 'all' :
        sets = set([i for i in range(1, 21)])
        
    elif type == 'empty' :
        sets = set()