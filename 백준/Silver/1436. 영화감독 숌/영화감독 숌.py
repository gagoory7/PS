#1436

a = int(input())
result = 666
cnt = 0

while True :
    if '666' in str(result):
        cnt +=1
    if cnt == a :
        break
        
    result +=1

print(result)