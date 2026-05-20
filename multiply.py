def multiply(x,y):
    if y==1:
        return x
    elif x==1:
        return y
    elif x==0 or y==0:
        return 0
    else:
        return x+(x,y,-1)