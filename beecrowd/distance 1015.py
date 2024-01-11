x,y = list(map(float,input().split()))
m,n =list(map(float,input().split()))
z = (((x-m)**2)+((y-n)**2))**(1/2)
print('%.4f'%z)