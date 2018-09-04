# number to find the factorial of
number = 6   
# start with our product equal to number
product = number

while  number > 1:
    # decrement number with each iteration until it reaches 1
    number -= 1
    # multiply the product so far by the current number
    product *= number

# print the factorial of number
print(product)
