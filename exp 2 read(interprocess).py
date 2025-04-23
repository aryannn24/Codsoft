# read.py
def main():
    try:
        with open("data.txt", "r") as file:
            for line in file:
                print("Received:", line.strip())
    except FileNotFoundError:
        print("data.txt not found. Run write.py first.")

if __name__ == "__main__":
    main()
