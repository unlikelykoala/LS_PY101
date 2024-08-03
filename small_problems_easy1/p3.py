'''
Print all even numbers from 1 to 99, inclusive, with each number on a separate line.
Bonus Question: Can you solve the problem by iterating over just the even numbers?
'''

# all
for i in range(1, 100):
    if i % 2 == 0:
        print(i)

# odd iteration
for i in range(2, 100, 2):
    print(i)
