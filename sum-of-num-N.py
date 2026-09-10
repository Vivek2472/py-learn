# sum of numbers from 1 to N
num = int(input("Enter a number: "))
sum = 0

# loop
for i in range(1, num+1):
    sum = sum + i

# print 
print(f"Sum of numbers from 1 to {num}: ", sum)
