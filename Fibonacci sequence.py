
def fibonacci(num):
    a = 0
    b = 1
    if num<=0:
        print('please enter number grator than zero')
    if num==1:
        print('febonacci is ',b)
    else:
        for i in range(1,num+1):
            print(a)
            c = a+b
            a = b
            b = c
fibonacci(7)