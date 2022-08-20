n=int(input('Enter the size : '))
list = []
ans = []
for i in range(n):
    list.append(input())
print(list)
j=0
for i in list:
    if i in ans:
        ans.append(i)
print(ans)
