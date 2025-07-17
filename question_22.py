user_input = int(input("Enter a decimal number: "))
binary = ""
n = user_input

if n == 0:
    binary = "0"
else:
    while n> 0:
        remainder= n%2
        binary = str(remainder) + binary
        n= n // 2
print(binary)
