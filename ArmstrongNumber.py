num=int(input("Enter a number to check armstrong or not:"))
check=num
sum=0
order=len(str(num))
while num>0:
    a=num%10
    sum+=a**order
    num=num//10
print(sum)
if(check==sum):
    print("Given number is armstrong:")
else:
    print("Number is not an armstrong:")