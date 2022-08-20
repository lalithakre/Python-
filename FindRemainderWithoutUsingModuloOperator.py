num1=int(input())
num2=int(input())
if num1>num2:
    rem=int(num1/num2)
    print("your answer is ",rem)
    rem=rem*num2
    rem=num1-rem
    print("Your remainder is",rem)
else:
    rem=int(num2/num1)
    print("your answer is ",rem)
    rem=rem*num1
    rem=num2-rem
    print("Your remainder is",rem)