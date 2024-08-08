import json
import os

# Open the JSON file for reading
with open('file.json', 'r') as file:
    MESSAGES = json.load(file)

def calc():
    # clear screen and welcome
    os.system('clear')
    print(MESSAGES['welcome'])

    # get operands and operator, validate input
    num1 = prompt(MESSAGES['num1']['first'])
    while invalid_number(num1):
        num1 = prompt(MESSAGES['num1']['invalid'])
    num1 = int(num1)

    num2 = prompt(MESSAGES['num2']['first'])
    while invalid_number(num2):
        num2 = prompt(MESSAGES['num2']['invalid'])
    num2 = int(num2)

    op = prompt(MESSAGES['operation']['first'])
    while invalid_operator(op):
        op = prompt(MESSAGES['operation']['invalid'])

    # Check for zero division
    while num2 == 0 and op == '4':
        fix = prompt(MESSAGES['fix_zero']['choice'])
        while fix not in ['1', '2']:
            fix = prompt(MESSAGES['fix_zero']['invalid'])
        if fix == '1':
            while invalid_number(num2) or num2 == 0:
                num2 = prompt(MESSAGES['num2']['mistake'])
            num2 = int(num2)
        else:
            while invalid_operator(op) or op == 4:
                op = prompt(MESSAGES['operation']['zero'])

    match op:
        case '1':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '2':
            print(f'{num1} - {num2} = {num1 - num2}')
        case '3':
            print(f'{num1} * {num2} = {num1 * num2}')
        case '4':
            print(f'{num1} / {num2} = {int(num1 / num2)}')

    again = prompt('Would you like to run calculator again?\n'
                   'y/n: ')
    while not again or again.casefold() not in ['y', 'n']:
        again = prompt(MESSAGES['again']['invalid'])
    if again == 'y':
        return calc()
    print('Thanks for using the calc() function!')
    return 0

def invalid_number(n_str):
    try:
        int(n_str)
    except ValueError:
        return True

    return False

def invalid_operator(operator):
    if operator not in ('1', '2', '3', '4'):
        return True
    return False

def prompt(message):
    return input(f'==> {message}')


calc()
