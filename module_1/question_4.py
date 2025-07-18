def even_no(x, y):
    """Get all even numbers between value and vertical_distance"""
    even_numbers = []
    for i in range(x, y + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

output = even_no(1000, 3000)
print(*output, sep=", ")
