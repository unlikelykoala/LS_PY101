'''
Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
The program must compute the tip, then print both the tip and the total amount of the bill. 
You can ignore input validation and assume that the user will enter valid numbers.
'''

# get bill and tip percentage
b = float(input('What is the bill? '))
tp = float(input('What is the tip percentage? ')) / 100
# calculate tip
tip = b * tp
# calc total
total = b + tip
# print
print(f'The tip is ${tip:.2f}\nThe total is ${total:.2f}')
