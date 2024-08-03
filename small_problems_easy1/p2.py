'''
Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
Bonus Question: Can you solve the problem by iterating over just the odd numbers?
'''

# all
for i in range(1, 100):
    if i % 2 == 1:
        print(i)

# odd iteration
for i in range(1, 100, 2):
    print(i)
