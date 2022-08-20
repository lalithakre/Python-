def knight(count,a,b,c,d):
    if (c>a & d>b):
        c=c-2
        d=d-1
        if (c==a & d==b):
            count=count+1
            print(count)
        else:
            knight(count,a,b,c,d)
    elif (c<a & d<b):
        c=c+1
        d=d+2
        if (c==a & d==b):
            count=count+1
            print(count)
        else:
            knight(count,a,b,c,d)
    elif (c==a & d==b):
            return count
    else:
        knight(count,a,b,c,d)
n=int(input("Enter size of Chessboards:"))
n=int(input("Enter size of Chessboards:"))
print("Enter initial position")
a=int(input())
b=int(input())
print("Enter target positions:")
c=int(input())
d=int(input())
count=0
print(knight(count,a,b,c,d))