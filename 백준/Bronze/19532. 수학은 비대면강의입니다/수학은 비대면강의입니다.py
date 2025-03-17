# 19532

x_1,y_1,c_1,x_2,y_2,c_2 = map(int,input().split())


y = int((c_1 *x_2 - c_2*x_1) / (y_1 * x_2 - y_2 * x_1) )
if x_1 != 0 :
    x = int((c_1 - y_1*y) / x_1)
else:
    x = int((c_2 -y_2*y ) / x_2)
    
print(x,y)