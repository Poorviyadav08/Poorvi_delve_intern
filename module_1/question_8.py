print("""
Enter the passwords you want to check separated by comma:
The suggested password should have:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12""")

user_input = input().split(',')
# print(user_input)
valid_passwords = []

for password in user_input:

    is_upper = False
    is_lower = False
    is_numeric = False
    special_char = False
    has_length = 6 <= len(password) <= 12

    for char in password:
        if char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
        elif char.isdigit():
            is_numeric = True
        elif char in "$#@":
            special_char = True

    if is_upper and is_lower and is_numeric and special_char and has_length:
        valid_passwords.append(password)

if valid_passwords:
    print(",".join(valid_passwords))
else:
    print("No valid passwords")

