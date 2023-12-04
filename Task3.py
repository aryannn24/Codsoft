import random
print("Welcome To Password Generator")
n=int(input("Please Enter the Length of The Password You Want: "))
password=""
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
for i in range(n):
        password = password + random.choice(char)
print(f"Generated Password is: {password}")