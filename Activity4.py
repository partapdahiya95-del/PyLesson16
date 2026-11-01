valid = False
while number % 2 == 0:
    try:
        number = int(input("Enter a number: "))
        while True:
            print("Bye")
    except ValueError:
        print("Invalid")