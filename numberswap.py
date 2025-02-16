# Function to swap three values
def swap_three_values(a, b, c):
    # Swapping values
    a, b, c = c, a, b
    return a, b, c

# Example usage
a = 10
b = 20
c = 30

print(f"Original values: a = {a}, b = {b}, c = {c}")

# Swap values and store in correct position
a, b, c = swap_three_values(a, b, c)

print(f"After swapping: a = {a}, b = {b}, c = {c}")
