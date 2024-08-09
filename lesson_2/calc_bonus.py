import json
from os import system
from sys import exit

# Open the json file for reading
with open('calc_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    return input(f'==> {message}')

def get_language():
    lang_choice = prompt('Press 1 for English or '
                         'Presione 2 para español: ')
    while lang_choice not in ['1', '2']:
        lang_choice = prompt('Try again. Press 1 for English\n'
                      'Presione 2 para español: ')
    if lang_choice == '1':
        return 'en'
    else: return 'es'

# get the language for MESSAGES dict key
lang = get_language()

def invalid_input(input_, input_type):
    match input_type:
        case 'number':
            try:
                int(input_)
            except ValueError:
                return True
            return False
        case 'operator':
            if input_ not in ('1', '2', '3', '4'):
                return True
            return False
        case _:
            print('Error: data_type entered incorrectly in the prompt call')
            exit(1)

def get_operand():
    n = prompt(MESSAGES[lang]['num']['first'])
    while invalid_input(n, 'number'):
        n = prompt(MESSAGES[lang]['num']['invalid'])
    return int(n)

def get_operator():
    operator = prompt(MESSAGES[lang]['operation']['first'])
    while invalid_input(operator, 'operator'):
        operator = prompt(MESSAGES[lang]['operation']['invalid'])
    return operator

def zerodiv_check(number, operation):
    while number == 0 and operation == '4':
        fix = prompt(MESSAGES[lang]['fix_zero']['choice'])
        while fix not in ['1', '2']:
            fix = prompt(MESSAGES[lang]['fix_zero']['invalid'])
        if fix == '1':
            while invalid_input(number, 'number') or number == 0:
                number = prompt(MESSAGES[lang]['num']['invalid'])
            number = int(number)
        else:
            while invalid_input(operation, 'operator') or operation == 4:
                operation = prompt(MESSAGES[lang]['operation']['zero'])
    return number, operation

def run_again():
    again = prompt(MESSAGES[lang]['again']['first'])
    if lang == 'en':
        while again.casefold() not in ['y', 'n']:
            again = prompt(MESSAGES[lang]['again']['invalid'])
    else:
        while again.casefold() not in ['s', 'n']:
            again = prompt(MESSAGES[lang]['again']['invalid'])
    if again.casefold() in ['s','y']:
        return True
    print(MESSAGES[lang]['goodbye'])
    return False
        

def main():
    # clear screen, language selection, welcome
    system('clear')
    print(MESSAGES[lang]['welcome'])

    # get operands and operator, validate input
    num1 = get_operand()
    num2 = get_operand()
    op = get_operator()

    # Check for zero division
    if num2 == 0 and op == '4':
        num2, op = zerodiv_check(num2, op)

    match op:
        case '1':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '2':
            print(f'{num1} - {num2} = {num1 - num2}')
        case '3':
            print(f'{num1} * {num2} = {num1 * num2}')
        case '4':
            print(f'{num1} / {num2} = {int(num1 / num2)}')

    if run_again(): main()
    else: return 0


main()
