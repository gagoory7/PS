#3009

x = []
y = []

# 좌표 입력 받기
for i in range(3):
    m, n = map(int, input().split())
    x.append(m)
    y.append(n)

# 중복되지 않는 좌표 찾기
unique_x = [coord for coord in x if x.count(coord) == 1]
unique_y = [coord for coord in y if y.count(coord) == 1]

# 결과 출력
print(unique_x[0], unique_y[0])