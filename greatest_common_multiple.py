def G_C_M(x,y):
    if x>y:
        small=y
    else:
        small=x
    while(True):
        if small%x==0 and small%y==0:
            lcm = small
            break
        small+=1
    print(lcm)
G_C_M(24,54)