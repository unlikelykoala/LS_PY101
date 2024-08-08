def calc():
    print('Welcome to the calculator!')

    num1 =prompt('Enter first integer: ')
    while invalid_number(num1):
        num1 = prompt('Please use integers only. First integer: ')
    num1 = int(num1)
    num2 = prompt('Enter second integer: ')
    while invalid_number(num2):
        num2 = prompt('Please use integers only. Second integer: ')
    num2 = int(num2)

    op = prompt('What operation would you like to perform?\n'
            '1: addition, 2: subtraction, 3: multiplication, 4: division\n'
            'Operation: ')
    while invalid_operator(op):
        op = prompt('Try again. Enter 1, 2, 3, or 4.\n'
                    '1: addition, 2: subtraction, 3: multiplication, ' 
                    '4: division\n'
                    'Operation: ')

    while num2 == 0 and op == '4':
        fix = prompt('Error: cannot divide by 0.\n'
            'Press 1 to change the second integer '
            'or Press 2 to change the operation: ')
        if fix == '1':
            while invalid_number(num2) or num2 == 0:
                num2 = prompt('Please use non-zero integers only. '
                                  'Second integer: ')
            num2 = int(num2)
        else:
            while invalid_operator(op) or op == 4:
                op = prompt('Try again. Enter 1, 2, or 3\n'
                    '1: addition, 2: subtraction, 3: multiplication\n'
                    'Operation: ')

    match op:
        case '1':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '2':
            print(f'{num1} - {num2} = {num1 - num2}')
        case '3':
            print(f'{num1} * {num2} = {num1 * num2}')
        case '4':
            print(f'{num1} / {num2} = {int(num1 / num2)}')

    again = input ('Would you like to run calculator again?\n'
                   'y/n: ')
    while again not in ['y', 'n']:
        again = input ('Try again. Enter y or n.\n'
                       'Would you like to run calculator again?\n'
                       'y/n: ')
    if again == 'y':
        return calc()
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
