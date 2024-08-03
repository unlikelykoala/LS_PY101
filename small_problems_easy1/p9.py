'''
Leap Year Part 2
'''
'''
def is_leap_year(y):
    if y < 1752:
        return y % 4 == 0
    elif y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    else: return y % 4 == 0


print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
'''

# Further exploration
# enter year and counrty code to determine if gregorian had started
def gregorian(y, c):
    match c:
        case 'JP':
            return y >= 1873
        case 'RU':
            return y >= 1867
        case _:
            return y >= 1582

# enter year and counrty code to determine if leap year
def is_leap_year(y, c):
    if not gregorian (y, c):
        return y % 4 == 0
    elif y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    else: return y % 4 == 0
