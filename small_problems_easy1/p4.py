'''
Build a program that asks the user to enter the length and width of a room, in meters, 
then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
'''

# get l and w in meters
l = int(input('Length of the room in meters: '))
w = int(input('Width of the room in meters: '))
# calculate sq meters
a_sqm = l * w
# calc sq feet
a_sqf = a_sqm * 10.7639
# print
print(f'The area is {a_sqm} square meters, or {a_sqf:.2f} square feet.')
