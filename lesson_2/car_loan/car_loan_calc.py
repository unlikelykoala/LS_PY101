import json
import math
from os import system

# Open the json file for reading
with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Clear console
system('clear')

def invalid_input(input_, type_):
    try:
        floated = float(input_)
        if math.isnan(floated):
            return True
    except (TypeError, ValueError):
        return True

    match type_:
        case 'principal':
            if '.' in input_:
                if len(input_.rsplit('.')[-1]) > 2:
                    return True
            if floated <= 0:
                return True
        case 'apr' | 'duration':
            if floated < 0:
                return True
    return False

def monthly_payment(princ, rate, months):
    if rate == 0 and months == 0:
        return princ
    if months == 0:
        return princ * (1 + rate)
    if mpr == 0:
        return princ / months
    return princ * (mpr / (1 - ((1 + rate)**(-months))))


# Get and validate principal, apr, duration
principal = input(MESSAGES['input']['principal'])
while invalid_input(principal, 'principal'):
    principal = input(MESSAGES['invalid'] + MESSAGES['input']['principal'])
apr = input(MESSAGES['input']['apr'])
while invalid_input(apr, 'apr'):
    apr = input(MESSAGES['invalid'] + MESSAGES['input']['apr'])
loan_duration_years = input(MESSAGES['input']['loan_duration_years'])
while invalid_input(loan_duration_years, 'duration'):
    loan_duration_years = input(MESSAGES['invalid']
                                + MESSAGES['input']['loan_duration_years'])

# Convert to useable format
principal = float(principal)
mpr = (float(apr) / 100) / 12  # monthly percentage rate in decimal format
loan_duration_months = math.ceil(float(loan_duration_years) * 12)

# Calculate monthly interest rate and payment
monthly_payment = monthly_payment(principal, mpr, loan_duration_months)

print(f'\n==>Your monthly payment will be USD ${monthly_payment:.2f} '
      f'over the course of {loan_duration_months} months.',)
