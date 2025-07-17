currency_input = input("Enter valid currencies in comma-separated form: ")
valid_currency = []
parts = currency_input.split(',')
for value in parts:
    value = value.strip()
    valid_currency.append(int(value))
money = int(input("Enter money amount: "))

def currency(valid_currency, money):
    """
    Finds minimum possible denominations for given currency
    """
    valid_currency.sort(reverse=True)
    result = []

    for amount in valid_currency:
        if money >= amount:
            count = money // amount
            result.append("{0}-{1}".format(amount, count))
            money = money % amount
    return result

output = currency(valid_currency, money)
for line in output:
    print(line)
