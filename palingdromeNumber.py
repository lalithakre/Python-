num=int(input("Enter a number to check palindrome or not:"))   #121
check=num   
answer=0
while num > 0:
    a=num%10
    answer=(answer*10)+a
    num=num//10
if(check==answer):
    print("Number is a palindrome:")
else:
    print("Number is not a palindrome:")