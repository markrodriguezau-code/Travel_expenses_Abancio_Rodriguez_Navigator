A = input("Enter Your Name: ")
print("Your name is", A)

B = input("Enter Your Destination: ")
print("Your Destination is", B)

C = float(input("Enter Your Budget: "))
print("Your Budget is", C)

if C <= 10000 and C > 0:
    travel = float(input("Enter Your Travel Expenses: "))
    other = float(input("Enter Your Other Expenses: "))
    food = float(input("Enter Your Food Expenses: "))

    total = travel + other + food

    print("Your Total Expenses are:", total)

    if total <= C:
        print("Your expenses are within your budget.")
        print("Your Remaining Budget is:", C - total)
    else:
        print("Warning: You exceeded your budget!")
        print("Your Excess Expenses are:", total - C)

else:
    print("Invalid Amount Budget! Please enter a budget from 1 to 10000.")