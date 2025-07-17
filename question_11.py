user_input = input("Enter the string: ").strip()

def count_chars(i):
    result =[]
    current_char = i[0]
    count = 1

    for char in i[1:]:
        if char == current_char:
            count+=1
        else:
            result.append(current_char.lower()+str(count))
            current_char = char
            count = 1
    result.append(current_char.lower()+str(count))
    return ''.join(result)


output = count_chars(user_input)
print("Output: {0}".format(output))