class Node:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.next=None

class Contact:
    def create(self):
        self.root=None

    def deletename(self,name):
        if self.root==None:
            print("Contact Book is Empty")
        elif self.root.name==name:
            m=self.root
            if(m.name==name):
                self.root=m.next
        else:
            t=self.root
            while(t.next.name!=name):
                t=t.next
            m=t.next.name
            t.next=t.next.next
            print(f'Contact is deleted')

    def deletephone(self,phone):
        if self.root==None:
            print("Contact Book is Empty")
        elif self.root.phone==phone:
            m=self.root
            if(m.phone==phone):
                self.root=m.next
        else:
            t=self.root
            while(t.next.phone!=phone):
                t=t.next
            m=t.next.phone
            t.next=t.next.next
            print(f'Contact is deleted')

    def insert(self,name,phone,email,address):
        n=Node(name,phone,email,address)
        if self.root==None:
            self.root=n
        else:
            t=self.root
            while(t.next!=None):
                t=t.next
            t.next=n
        print("Contact added to Book")

    def print(self):
        if self.root == None:
            print("Contact Book is Empty")
        else:
            t=self.root
            print("Name\t\t\t\tPhone\t\t\t\tEmail\t\t\t\t\tAddress")
            print("------------------------------------------------------------------------------------------------")
            while(t.next!=None):
                print(t.name, "\t\t\t", t.phone, "\t\t", t.email, "\t\t", t.address)
                t=t.next
            print(t.name, "\t\t\t", t.phone, "\t\t", t.email, "\t\t", t.address)
            print("------------------------------------------------------------------------------------------------")

    def update(self,name):
        t = self.root
        while (t != None):
            if (name == t.name):
                a=int(input("1.Name\n2.Phone\n3.Email\n4.Address\nEnter Your Option "))
                if(a==1):
                    t.name=input("Enter")
                    print("Updated Successfully")
                    break
                elif(a==2):
                    t.phone=input("Enter")
                    print("Updated Successfully")
                    break
                elif (a==3):
                    t.email=input("Enter")
                    print("Updated Successfully")
                    break
                elif (a==4):
                    t.address=input("Enter")
                    print("Updated Successfully")
                    break
            else:
                t = t.next
        else:
            print("No Such Contact Found in The Book")

    def searchname(self,name):
        t=self.root
        while(t!=None):
            if(name==t.name):
                print("Contact is found")
                print("Name\t\t\t\tPhone\t\t\t\tEmail\t\t\t\t\tAddress")
                print("-------------------------------------------------------------------------------------")
                print(t.name, "\t\t\t", t.phone, "\t\t", t.email, "\t\t", t.address)
                print("-------------------------------------------------------------------------------------")
                break
            else:
                t=t.next
        else:
            print("No Such Contact Found in The Book")

    def searchphone(self,phone):
        t=self.root
        while(t!=None):
            if(phone==t.phone):
                print("Contact is found")
                print("Name\t\t\t\tPhone\t\t\t\tEmail\t\t\t\t\tAddress")
                print("-------------------------------------------------------------------------------------")
                print(t.name, "\t\t\t", t.phone, "\t\t", t.email, "\t\t", t.address)
                print("-------------------------------------------------------------------------------------")
                break
            else:
                t=t.next
        else:
            print("No Such Contact Found in The Book")

a=Contact()
a.create()
print("Welcome To Our Contact Book")
while True:
        print("1.Add\n2.View\n3.Search\n4.Update\n5.Delete\n6.Stop")
        n = int(input("Enter your choice: (1/2/3/4/5/6) "))
        if (n == 1):
            name=input("Enter name ")
            phone=input("Enter phone ")
            email=input("Enter email ")
            address=input("Enter address ")
            a.insert(name,phone,email,address)

        elif (n == 2):
            a.print()

        elif (n == 3):
            print("Enter Choice\n1.Name\n2.Phone")
            c=int(input("Enter (1/2) "))
            if(c==1):
                name=input("Enter name")
                a.searchname(name)
            elif(c==2):
                phone=input("Enter phone")
                a.searchphone(phone)
            else:
                print("Invalid Choice")

        elif (n == 4):
            name = input("Enter name")
            a.update(name)

        elif (n == 5):
            print("Enter Choice\n1.Name\n2.Phone")
            b=int(input("Enter (1/2) "))
            if (b == 1):
                name = input("Enter name")
                a.deletename(name)
            elif (b == 2):
                phone = input("Enter phone")
                a.deletephone(phone)
            else:
                print("Invalid Choice")

        elif (n == 6):
            print("Thank You For Using Contact Book")
            break
        else:
            print("Enter correct option")