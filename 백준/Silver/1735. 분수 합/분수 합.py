# 1735

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

c = y1 * y2

u = x1*y2 + x2*y1

a ,b = c,u

while b > 0:
    a,b = b, a%b



print(str(int(u/a))+' '+str(int(c/a)))