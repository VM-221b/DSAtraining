def expo(x,y):
    if x==0:
        return 
    elif y==0:
        return 1
    elif y==1:
        return x
    elif x==1:
        return 1
    else:
        return x*expo(x,y-1)