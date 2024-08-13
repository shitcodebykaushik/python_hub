 # Python program to finsd the HCF of two number 


num1 = input()
num2 =input()
a = num1
b = num2
while num1 != num2:
    if num1>num2:
        num1-=num2
    else :
        num2 -= num1
print (num1)