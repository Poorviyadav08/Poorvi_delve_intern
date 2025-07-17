user_input = input("Enter comma separated sequence of words as input:")
words = user_input.split(",")

# seperator = ","
sorted_output = ",".join(sorted(words))
print(sorted_output)