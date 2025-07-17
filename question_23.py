user_input= int(input("Enter a number: "))

divisor_sum = 0
for i in range(1, user_input):
    if user_input % i== 0:
        divisor_sum+=i
if divisor_sum == user_input:
    print("Perfect number")
else:
    print("Not a perfect number")
