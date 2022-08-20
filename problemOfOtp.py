str=input("Enter a number :")
lst=[]
odd_places=[]
for i in range (0,len(str),2):
    lst.append(str[i])
odd_places=list(map(int,lst))
for i in range(len(odd_places)):
    odd_places[i]=odd_places[i]**2
str_otp=""
for i in odd_places:
    str_otp+=f"{i}"
print(str_otp)
print(f"OTP:{str_otp[:4]}")