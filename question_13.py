def binary_pairs(user_input):
    """
    Finds the number of pairs that starts and end with 1
    :param user_input: the input string
    :return: number of pairs
    """
    count_ones = 0
    for char in user_input:
        if char == '1':
            count_ones += 1
    return count_ones * (count_ones - 1) // 2
user_input = input("Enter binary string:")
print(binary_pairs(user_input))
