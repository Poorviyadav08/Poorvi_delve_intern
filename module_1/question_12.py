def sum_9(user_input):
    result = []
    letters = []

    for i in range(len(user_input)):
        if user_input[i].isalpha():
            letters.append((i, user_input[i]))
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            start = letters[i][0]
            end = letters[j][0]
            sum = 0
            for char in user_input[start + 1:end]:
                if char.isdigit():
                    sum +=int(char)
            if sum ==9:
                result.append(f"{letters[i][1]},{letters[j][1]}")
    return result

user_input = input("Enter the string: ")
sum_9_pairs = sum_9(user_input)

for pair in sum_9_pairs:
    print(pair)

