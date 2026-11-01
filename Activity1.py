try:
    number = int(input("Enter a number: "))
    print("The number you have entered:",number)
except ValueError as ex:
    print("Exception:",ex)