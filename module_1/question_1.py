result=[]
def two_d_array(x,y):
    """Generate a 2-dimensional array"""
    for i in range(x):
        rows = []
        for j in range(y):
            rows.append(i*j)
        result.append(rows)
    return result

user_input = input("Enter two numbers separated by a comma:")
x, y = user_input.split(",")
x = int(x)
y = int(y)

# print(value)
# print(vertical_distance)

if x>0 and y>0:
    array = two_d_array(x,y)
    print(array)
else:
    print("Please enter non negative numbers:")