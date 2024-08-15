numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

n2 = numbers[-1: :-1]
print(n2)

n3 = list(reversed(numbers))
print(n3)

reversed_numbers = numbers[::-1]
print(reversed_numbers)
