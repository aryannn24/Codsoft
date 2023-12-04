import random
game=["Rock","Paper","Scissors"]
t=c=u=0
while(1):
    m=input("Do you want to play? (Yes/No)")
    if m=="Yes":
        t=t+1
        print("1.Rock\n2.Paper\n3.Scissors\nEnter Your Choice:(1/2/3)")
        n=int(input())
        comp=random.choice(game)
        print(f"Computer's Choice: {comp}")
        if(n==1):
            if(comp=="Paper"):
                print("User Lose")
                c=c+1
            elif(comp=="Scissors"):
                print("User Win")
                u=u+1
            else:
                print("Tie")
        elif(n==2):
            if (comp == "Rock"):
                print("User Win")
                u=u+1
            elif (comp == "Scissors"):
                print("User Lose")
                c=c+1
            else:
                print("Tie")
        elif (n == 3):
            if (comp == "Rock"):
                print("User Lose")
                c=c+1
            elif (comp == "Paper"):
                print("User Win")
                u=u+1
            else:
                print("Tie")
        else:
            print("Invalid Choice")

    elif m=="No":
        break

    else:
        print("Invalid Choice")

print(f"Total Matches Played: {t}")
print(f"User Wins: {u}")
print(f"Computer Wins: {c}")


