initialBalance = int(input("enter the balance: "))
while True:
    operation = input("enter the operation [withdraw / w , deposit / d]:")
    if str(operation).upper() == "W":
        amount = int(input("enter the amount to withdraw: "))
        if amount <= initialBalance:
            initialBalance = initialBalance - amount
            print("your new balance is ", initialBalance)
        elif amount > initialBalance:
            print("error: no enough money to withdraw")
    elif str(operation).upper() == "D":
        amount = int(input("enter the amount to deposit: "))
        initialBalance = initialBalance + amount
        print("your new balance is ", initialBalance)
    else:
        if operation == "":
            break
        else:
            print("wrong operation")