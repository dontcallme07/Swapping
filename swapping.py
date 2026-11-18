# Program to swap two numbers
# Get two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display values before swapping
print("\nBefore swapping:")
print("First number =", a)
print("Second number =", b)

# Swap the values
a, b = b, a

# Display values after swapping
print("\nAfter swapping:")
print("First number =", a)
print("Second number =", b)