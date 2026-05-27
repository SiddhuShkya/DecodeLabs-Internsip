curr_amount = 1000
print(f"Initial balance: $ {curr_amount}")
while True:
    try:
        user_input = input("Enter expense amount (type q to quit): ")
        if user_input.lower() == "q":
            break
        expense = int(user_input)
        curr_amount -= expense
        print(f"Expense added. Current balance: $ {curr_amount}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"\nFinal balance: $ {curr_amount}")
