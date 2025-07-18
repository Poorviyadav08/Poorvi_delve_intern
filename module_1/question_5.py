user_input = input("Enter a sentence to calculate the number of letters and digits it contain:").casefold()
letters = 0
digits = 0
for i in user_input:
    if i.isalpha():
        letters += 1
    elif i.isnumeric():
        digits += 1

print("LETTERS {0}".format(letters))
print("DIGITS {0}".format(digits))