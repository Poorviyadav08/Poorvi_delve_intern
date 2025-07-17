net_amount = 0
print("Enter the transaction amount in the format 'D AMOUNT' or 'W AMOUNT':")
print("Enter 0 to finish and see the total balance.\n")

transaction = True
while transaction:
    user_input = input()
    if user_input == "0":
        break

    try:
        operation, amount = user_input.split()
        amount = int(amount)
        if operation.upper() == "D":
            net_amount+= amount
        elif operation.upper() == "W":
            net_amount -= amount
        else:
            print("Invalid transaction type. Use 'D' for deposit or 'W' for withdrawal.")
    except ValueError:
        print("Invalid Input format")
print("Net amount in bank account: {0}".format(net_amount))

