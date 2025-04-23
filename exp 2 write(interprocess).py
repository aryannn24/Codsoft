# write.py
def main():
    with open("data.txt", "w") as file:
        print("Enter text (type 'exit' to stop):")
        while True:
            user_input = input()
            if user_input.lower() == "exit":
                break
            file.write(user_input + "\n")
    print("Data written to data.txt")

if __name__ == "__main__":
    main()
