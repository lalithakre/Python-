num=str(input())
final=""
lst=num.split(',')
for i in lst:
    name=i.split(":")[0]
    code=i.split(":")[1]
    max=0
    for i in code:
        if int(i)<=len(name):
            if int(i)>max:
                max=int(i)
    if max==0:
        final=final+"X"
    else:
        final=final+name[max-1]
    print(final)