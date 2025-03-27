s = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia :
    s = s.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(s))