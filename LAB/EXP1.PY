print("Name : Lalit Thakre")
print("Enrollment number : 0536CS201016")
books_list=[]

class library1:
    def __init__(self,t,a,p,pag,pub):
        self.title=t
        self.author=a
        self.price=p
        self.pages=pag
        self.published_date=pub

print('Welcome To The Library Management System: ')
print("Press '1' : To Add a new Book ")
print("Press '2' : To Remove a Book ")
print("Press '3' : To view list of Books ")
print("Press '4' : To Exit the menu ")

while 1:
    num=input('\nEnter which action you wanna perform: ')
    if num=='1':
        t=input("\nEnter the Title of the Book ")
        a=input("Enter the Author of the Book ")
        p=input("Enter the Price of the Book ")
        pag=input("Enter the Pages of the Book ")
        pub=input("Enter the Published Date of the Book ")
        books_list.append(library1(t,a,p,pag,pub))
        print("\n**Your Book is added successfully**")
    elif num=='2':
        t=input("\nEnter the Title of the Book ")
        a=input("Enter the Author of the Book ")
        p=input("Enter the Price of the Book ")
        pag=input("Enter the Pages of the Book ")
        pub=input("Enter the Published Date of the Book ")
        if (t,a,p,pag,pub in books_list):
            books_list.remove(library1(t,a,p,pag,pub))
            print("\n**Book is deleted from the Library Successfully**")
        else:
            print("\n**Invalid Book**")
    elif num=='3':
        for i in books_list:
            print("\nBook Title - ",i.title)
            print("Book Author - ",i.author)
            print("Book Price - ",i.price)
            print("Book Pages - ",i.pages)
            print("Book Published Date - ",i.published_date)
    elif num=='4':
        print('\nThankyou...')
        break
    else:
      print('\n**Invalid Choice**')