sample_data = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}

print("Please enter your test values:")
patient_data = {}
for key in sample_data:
    value = int(input("{0}: ".format(key)))
    patient_data[key] = value

difference = {}
for key in sample_data:
    difference[key] = sample_data[key] - patient_data[key]

print(difference)
print()
for key, diff in difference.items():
    if diff == 0:
        print("{0} is at the ideal value.\n".format(key))
    elif diff > 0:
        print("{0} -{1}".format(key, diff))
        print("The {0} is {1} less than the ideal value.\n".format(key.lower(), diff))
    else:
        print("{0} {1}".format(key, abs(diff)))
        print("The {0} is {1} more than the ideal value.\n".format(key.lower(), abs(diff)))
