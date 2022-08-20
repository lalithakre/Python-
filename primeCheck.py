num=int(input("Enter a number to check prime number or not :"))
num1=(num/2)
if num>1:
    while num1 < num:
        if((num%num1)!=0):
            print("your number is a prime number:")
        else:
            num1=num1+1
        num1=num1+1
    else:
        print("Number is not prime number")