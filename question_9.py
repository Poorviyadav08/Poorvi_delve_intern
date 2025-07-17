print("""
Enter(name, age, height) tuples separated by commas:
Enter 0 to get the sorted data.
""")

data = []
while True:
    user_input = input()
    if user_input == "0":
        break
    try:
        name, age, score = user_input.split(",")
        data.append((name.strip(), int(age), int(score)))
    except ValueError:
        print("Invalid Input.")

sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

print(sorted_data)