user_input = input("Enter movements for movement separated by comma: ").split(',')

horizontal_distance = 0
vertical_distance = 0

for command in user_input:
    command = command.strip()
    try:
        direction, steps = command.split()
        steps = int(steps)

        if direction.upper() == "UP":
            vertical_distance += steps
        elif direction.upper() == "DOWN":
            vertical_distance -= steps
        elif direction.upper() == "LEFT":
            horizontal_distance -= steps
        elif direction.upper() == "RIGHT":
            horizontal_distance += steps
        else:
            print("Invalid direction: {0}".format(direction))
    except ValueError:
        print("Invalid Input")

distance = round((horizontal_distance ** 2 + vertical_distance ** 2) ** 0.5)
print("Distance from origin: {0}".format(distance))
