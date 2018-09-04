# number we'll find the factorial of
number = 6
# start with our product equal to number
product = number

# calculate factorial of number with a for loop
for num in range(1, number):
    product *= num

# print the factorial of number
print(product)
