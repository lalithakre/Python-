from operator import concat


num=input("Enter a code as following sequence: # lalit:1234\n")
sum=0
num1=num.find(':')
if(num1==-1):
    print("Please enter valid code:")
else:
    num2=num.split(':')
    num3=str(num2[1])
    num4=str(num2[0])
    len=len(num4)
    if num2[1].isdigit()&num2[0].isalpha():
        num5=int(num2[1])       #bcdgfhf:127836
        while num5>0:
            a=num5%10
            sum+=a*a
            num5=num5//10
        if (sum%2==0):
            print("even\n")
            num5=num[len-2:len]
            num6=num[0:len-2]
            print(concat(num5,num6))
        else:
            num5=num[0]
            num6=num[1:len]
            print(concat(num6,num5))
    else:
        print("Please enter valid code:")