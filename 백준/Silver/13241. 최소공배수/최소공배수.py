# 13241

m,n = map(int,input().split())
c = m *n
while n > 0:
    m,n = n, m %n

print( int( c/ m) )