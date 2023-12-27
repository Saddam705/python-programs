print('enter a number which is value 1')
num1 = int(input())
print('enter value 2')
num2 = int(input())
temp = 0
if num1>num2:
    temp = num2
else:
    temp=num1
val = 0
for i in range(1,temp+1):
    if  num1%i==0 and num2%i==0:
        val=i
print('the largest devisible values is',val)
