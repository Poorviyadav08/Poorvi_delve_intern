user_input = input("Enter a sentence:")
upper_case = 0
lower_case = 0
for i in user_input:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1


print("UPPER CASE: {0}".format(upper_case))
print("LOWER CASE: {0}".format(lower_case))