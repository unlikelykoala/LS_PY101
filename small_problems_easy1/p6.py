'''
Write a program that asks the user to enter an integer greater than 0, 
then asks whether the user wants to determine the sum or the product of 
all numbers between 1 and the entered integer, inclusive.
'''
'''
# get num
num = int(input('Please enter an integer greater than 0: '))
while num <= 0:
    num = int(input('Try again. Please enter an integer greater than 0: '))

# operation: sum or product
operator = input('Enter "s" to compute the sum, or "p" to compute the product. ')

# sum
if operator == 's':
    sum = sum(range(1, num + 1))
    print(f'The sum of the integers between 1 and {num} is {sum}.')

# product
else:
    product = 1
    for i in range(1, num + 1):
        product *= i
    print(f'The product of the integers between 1 and {num} is {product}.')
'''
'''
Suppose the input was a list of space separated integers instead of just a single integer? 
How would your compute_sum and compute_product functions change?
'''

def get_sum(x):
    return sum(x)
    
def get_prod(x):
    prod = 1
    for i in x:
        prod *= i
    return prod

# get num
num = int(input('Please enter an integer greater than 0: '))
while num <= 0:
    num = int(input('Try again. Please enter an integer greater than 0: '))

# change to space-separated list
numbers = " ".join(list(range(1, num + 1)))

# operation: sum or product
operator = input('Enter "s" to compute the sum, or "p" to compute the product. ')

# sum
if operator == 's':
    sum = get_sum(numbers)
    print(f'The sum of the integers between 1 and {num} is {sum}.')

# product
else:
    product = get_prod(numbers)
    print(f'The product of the integers between 1 and {num} is {product}.')

