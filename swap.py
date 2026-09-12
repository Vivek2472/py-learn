# swapping two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# before swap
print("Before first number: ", a, ",second number: ", b)

# swap
a, b = b, a

# print
print("After swapping two numbers, first number: ",a, ",second number: ", b)
