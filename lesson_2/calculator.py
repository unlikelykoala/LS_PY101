print('Welcome to the calculator!')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('What operation would you like to perform?\n'
           '1: addition, 2: subtraction, 3: multiplication, 4: division ')

match op:
    case '1':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '2':
        print(f'{num1} - {num2} = {num1 - num2}')
    case '3':
        print(f'{num1} * {num2} = {num1 * num2}')
    case '4':
        print(f'{num1} / {num2} = {int(num1 / num2)}')
    case _:
        print('Please input the addition, subtraction,'
              'mulitiplication, or division operator')
