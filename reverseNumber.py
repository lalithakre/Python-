from traceback import print_tb


a=int(input("Enter a number "))
answer=0

while a>0:
    n=a%10
    answer=(answer*10)+n
    a=a//10
print(answer)