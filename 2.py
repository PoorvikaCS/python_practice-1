a=8
b=6
print(a+b)
print(a-b)
print(a%b)
print(a/b)
print(a//b)
print(a*b)
print(a**b)

# Swapping without a third variable
a = 5
b = 10

# Print values before swapping
print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Using tuple unpacking to swap values
# temp = a
# a = b
# b = temp  (swapping with third variable)
a, b = b, a

# Print values after swapping
print("\nAfter swapping without third variable:")
print("a =", a)
print("b =", b)



a = 19
b = 12
# Using the correct BODMAS order
result = a - b + a * (a // b) * (a % b) / a
print(result)



