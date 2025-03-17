def convert(value):
    try:
        return int(value)  # 숫자로 변환 시 숫자 반환
    except ValueError:
        return value  # 변환할 수 없으면 문자열 그대로 반환
    

num_list = []

for i in range(3) :
    _ = input()
    num_list.append(convert(_))


loc = 0 
num = 0
for index, item in enumerate(num_list):
    if isinstance(item, int):  # 숫자이면
        loc, num = index, item
        
while loc <=2  :
    num+=1
    loc +=1


if (num % 5 == 0 )and (num % 3 == 0 ) :
    print('FizzBuzz')
elif num % 5 == 0 :
    print('Buzz')
elif num % 3 == 0 :
    print('Fizz')
else : 
    print(num)