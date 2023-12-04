print("Welcome! This Calculator is Created By Aryan")
while(1):
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Stop")
    n = int(input("Enter choice of operation (1/2/3/4) "))
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    if(n==1):
        print(f"Addition:{a+b}")
    elif(n==2):
        print(f"Subtraction:{a-b}")
    elif(n==3):
        print(f"Multiplication:{a*b}")
    elif(n==4):
        print(f"Division:{a/b}")
    elif(n==5):
        break
    else:
        print("Enter correct option")

print("Thank You For Using Our Calculator")

