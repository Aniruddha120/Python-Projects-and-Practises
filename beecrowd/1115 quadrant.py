x,y = list(map(int,input().split()))
while x!=0 or y!= 0:
    if x >0 and y>0:
        print('primeiro')
    
    elif x >0 and y<0:
        print('quarto') 
    elif x <0 and y<0:
        print('terceiro')    
    elif x <0 and y>0:
        print('segundo')
    x,y = list(map(int,input().split()))

