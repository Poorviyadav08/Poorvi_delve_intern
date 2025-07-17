n = int(input("Enter total number of stops (n): "))
m = int(input("Enter number of stops the bus must make (m): "))

def combinations(a, b):
    if b > a or b < 0:
        return 0
    result = 1
    for i in range(1, b + 1):
        result *=(a - i + 1)
        result //= i
    return result

def non_consecutive_combinations(n, m):
    if m == 0:
        return 1
    if m > n:
        return 0
    return combinations(n - m + 1, m)

print("Number of ways the bus can travel so that no stop is consecutive:", non_consecutive_combinations(n, m))

