user_input = input("Enter email address: ")
def valid_email(email):
    if email.count('@') != 1:
        return False
    chars = "abcdefghijklmnopqrstuvwxyz0123456789._"
    for ch in email:
        if ch.isupper():
            return False
        if ch not in chars and ch != '@':
            return False
    return True

if valid_email(user_input):
    print("Valid email address.")
else:
    print("Invalid email address.")
