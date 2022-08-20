n=int(input())
arr=[]
print("Enter Matrix elements:")
for i in range(0,n):
    a=[]
    for j in range(0,n):
        a.append(int(input()))
    arr.append(a)
print("Before rotating list elements are:")
for i in range(0,n):
    for j in range(0,n):
        print(arr[i][j],end=" ")
    print("")
print("After Anticlockwise 90 degree rotating list elements are:")
j=n
while j>0:
    j=j-1
    i=0
    while i<n:
        print(arr[i][j],end=" ")
        i=i+1
    print("")