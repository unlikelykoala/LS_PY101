'''
Write a function that computes the sum of all numbers between 1 and some other number, 
inclusive, that are multiples of 3 or 5. 

For instance, if the supplied number is 20, 
the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1
'''

def multisum(n):
    lst = list(range(1, n + 1))
    lst2 = []
    for i in lst:
        if i % 3 == 0 or i % 5 == 0:
            lst2.append(i)
    
    return sum(lst2)


print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
