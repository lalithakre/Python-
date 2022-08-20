'''
    class student:
        def __init__(self,m1,e1,h1):
            self.maths=m1
            self.english=e1
            self.hindi=h1
        def __add__(self):
             m=self.maths+self.english+self.hindi
            a=student(m)
            return a
    s1=student(24,35,57)
    s2=student(43,54,65)
    a=s1.maths+s1.english+s1.hindi
    b=s2.maths+s2.english+s2.hindi
    if a>b:
        print("A is winner")
    else:
         print("B is winner")
'''
class A:
    def __init__(self, h,e,m):
        self.h = h
        self.e=e
        self.m=m
    def __gt__(self, other):
        a=self.h+self.e+self.m
        b=self.h+self.e+self.m
        if(a>b):
            return True
        else:
            return False
ob1 = A(87,67,97)
ob2 = A(87,96,76)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")