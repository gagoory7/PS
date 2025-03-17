a = input()
result = []
count = 0
for x in list(a):
    if x == '<' :
        if result :
            print(''.join(result[::-1]),end='')
            result = []
        result.append(x)
        count = 1
        continue
    elif x == '>' :
        result.append(x)
        count = 0
        print(''.join(result),end='')
        result = []
        continue

    if count == 1 :
        result.append(x)
        continue

    if count == 1 and x == ' ' :
        result.append(x)
        continue

    if count == 0 and x == ' ' :

        print(''.join(result[::-1]),end=' ')
        result = []
        continue

    elif count == 0 and x != ' ' :
        result.append(x)
        continue

print(''.join(result[::-1]))