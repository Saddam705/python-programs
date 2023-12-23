def armstrong_num(num):
    length = len(str(num))
    add = 0
    tem=num
    while tem>0:
        digit = tem%10
        add += digit**length
        tem = tem//10
    if add==num:
        print(num,'armstrong number')
    else:
        print(num,"not a armstrong number")

armstrong_num(1634)