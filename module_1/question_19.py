def string(direction, text, times):
    for i in range(times):
        if direction == 1:
            text = text[1:] + text[0]
        elif direction == 2:
            text = text[-1] + text[:-1]
        else:
            print("Invalid")
            return
        print(text)

direction = int(input("Enter rotation direction (1:left, 2:right): "))
text = input("Enter the string: ")
times = int(input("Enter number of rotations: "))

string(direction, text, times)
