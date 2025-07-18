num_input= int(input("Enter a number: "))
num_str = str(num_input)
num_digits = len(num_str)

armstrong_sum = 0
for digit in num_str:
    armstrong_sum += int(digit) ** num_digits
if armstrong_sum == num_input:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
