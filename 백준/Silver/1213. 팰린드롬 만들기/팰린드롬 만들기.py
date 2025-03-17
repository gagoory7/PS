name = input()

count = dict()
keys = sorted(list(set(name)))
odd = []

for key in keys:
    cnt = name.count(key)
    count[key] = cnt
    if cnt % 2:
        odd.append(key)

if len(odd) > 1 :
    print('I\'m Sorry Hansoo')

else :
    result = ''
    
    for key in keys:
        result += key * (count[key]//2)
    
    if odd :
        result += odd[0] + result[::-1]
    else :
        result += result[::-1]

    print(result)