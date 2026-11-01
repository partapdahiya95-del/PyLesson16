try:
    first_num = int(input("Enter a number: "))
    second_num = int(input("Enter a second number: "))
    print(first_num, second_num)
    division = first_num / second_num
    print(division)
except ZeroDivisionError:
    print("Division by zero is error !!")
except ValueError:
    print("Enter a valid whole number.")
except:
    print("Wrong input.")
else:
    print("No exceptions.")
finally:
    print("This will execute no matter what.")