def sum(N):
    if N==0:
        return 0
    elif N==1: 
        return 1
    else:
        return N+sum(N-1)