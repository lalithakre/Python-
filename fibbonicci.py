a,b=0,1
i=2
num=int(input("enter range of fibbonici series:"))
print(a)
print(b)
while i < num:
    sum=a+b
    a=b
    print(sum)
    b=sum
    i=i+1