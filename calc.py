# imports

# global vars



# functions
def print_menu():
    print("-----------------------------")
    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiplication")
    print("[4] Division")
    print("-----------------------------")


# plains instructions
print_menu()
opt = input("Select an option: ")


num1 = float(input("Please provide num 1:"))
num2 = float(input("Please provide num 2:"))

if opt == "1":
    total = num1 + num2
    print("The total is: " + str(total))
    

elif opt == "2":
    total = num1 - num2
    print("The total is: " + str(total))

elif opt == "3":
    total = num1 * num2
    print("The total is: " + str(total))

elif opt == "4":
    if num2 == 0:
        print("Erooro: don't divide by zero")
    else:
        total = num1 / num2
        print("The total is: " + str(total))
    