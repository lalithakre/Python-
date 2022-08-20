from tabnanny import check


num=int(input())
check=int(num/2)
check=check*2
check=abs(check-num)
print(check)
if check==1:
    print("Odd")
else:
    print("Even")