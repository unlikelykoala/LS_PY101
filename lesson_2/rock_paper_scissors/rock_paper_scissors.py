import cowsay
import json
import random
import time
from os import system
from tabulate import tabulate

# Open the json file for reading
with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

system('clear')

# get name and initialize constants and global vars
NAME = input('Howdy, partner! What\'s yer name? ')
while not NAME:
    NAME = input('Don\'t be shy! What\'s yer name? ')
COMPUTER = MESSAGES['computer_name'][random.choice(['1', '2', '3', '4'])]
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
WIN_NUMBER = 3

scores = {
    NAME : 0,
    COMPUTER : 0,
    'Tie' : 0
}

def see_instructions():
    response = input('Wanna take a gander at them instructions? (y/n) ')
    while response.casefold() not in ['y', 'n']:
        response = input('Whoopsie-daisy! How about tryin\' that again?\n'
                     'Wanna see that there explainer? (y/n) ')
    
    if response.casefold() == 'y':
        system('clear')
        return True
    system('clear')
    return False

def keep_going():
    keep_going = input('Press c to continue: ')
    while not keep_going or keep_going.casefold() != 'c':
        keep_going = input('Just lemme know when you\'re ready!\n'
                         'Press c to continue: ')

def display_instructions():
    for win_tool, dict_ in MESSAGES['verb'].items():
        for lose_tool, action in dict_.items():
            print(f'--{win_tool} {action} {lose_tool}')
    keep_going()
    print()


def is_invalid(choice_):
    try:
        int_choice = int(choice_)
        if int_choice not in range(1, 7):
            return True
    except (TypeError, ValueError):
        return True
    return False

def get_player_choice():
    system('clear')
    print(f'Choose yer tool of reckoning:')
    for index, weapon in enumerate(VALID_CHOICES, start=1):
        print(f'{index}. {weapon}', sep=', ')
    print('6. See instructions\n')
    
    choice = input('Pick a number \'tween 1 and 6: ')
    print()

    while choice == '6' or is_invalid(choice):
        while choice == '6':
            display_instructions()
            for index, weapon in enumerate(VALID_CHOICES, start=1):
                print(f'{index}. {weapon}', sep=', ')
            print('6. See instructions')
            choice = input('Pick a number \'tween 1 and 6: ')

        while is_invalid(choice):
            print(MESSAGES['error'][random.choice(['1', '2', '3', '4'])])
            choice = input(f'Choose yer tool of reckoning!\n'
                        'Pick a number \'tween 1 and 6: ')
    
    return VALID_CHOICES[int(choice) - 1]

def get_winner(player, computer):
    if player == computer:
        return 'Tie', player, computer
    
    elif (player == 'rock' and computer in ['scissors', 'lizard']) or \
        (player == 'scissors' and computer in ['paper', 'lizard']) or \
        (player == 'paper' and computer in ['rock', 'Spock']) or \
        (player == 'lizard' and computer in ['paper', 'Spock']) or \
        (player == 'Spock' and computer in ['rock', 'scissors']):
        return(NAME), player, computer

    return COMPUTER, computer, player

def countdown():
    countdown = [3, 2, 1]
    for n in countdown:
        print(f'{n}... ', sep='')
        time.sleep(0.6)
    print('Draw!')
    time.sleep(0.4)
    system('clear')  

def display_winner(champ, win_choice, lose_choice):
    if champ == 'Tie':
        print('It\'s a tie!\n'
              f'{win_choice} does nothing to {lose_choice:}.')
    else:
        print(f'{win_choice.title()} '
                f'{MESSAGES['verb'][win_choice][lose_choice]} '
                f'{lose_choice}!\n'
                f'{champ} wins!')
    keep_going()

def display_scores():
    lst = [[key, value] for key, value in scores.items()]
    print(tabulate(lst, headers=['', 'Score'], tablefmt="heavy_grid"))
    keep_going()

def play_again(champ):
    system('clear')
    global COMPUTER
    if NAME == champ:
        print('That\'s 3 out of 5! You\'re the new champ!')
        time.sleep(0.5)
        print(f'You beat {COMPUTER}! Looks like there\'s a new sheriff in town!')
    if COMPUTER == champ:
        print(f'Game over! Sorry, {NAME}, that\'s 3 out of 5!')
        time.sleep(0.5)
        print(f'Looks like {COMPUTER} is still the best in the biz.')
    response = input('You up for another go? (y/n) ')
    while response.casefold() not in['y', 'n']:
        response = input('Whoopsie-daisy! How about tryin\' that again?'
                     'You up for another go? (y/n) ')
    
    if response.casefold == 'y':
        COMPUTER = MESSAGES['computer_name'][random.choice(['1', '2', '3', '4'])]
        main()
    else:
        print(cowsay.cow('So long, space cowboy!'))
        return 'end'

def best_of_five():
    player_choice = get_player_choice()

    computer_choice = random.choice(VALID_CHOICES)

    winner, win_weapon, lose_weapon = get_winner(player_choice, computer_choice)
    countdown()
    display_winner(winner, win_weapon, lose_weapon)

    # update and print scores table
    scores[winner] += 1
    display_scores()

    if scores[winner] == WIN_NUMBER:
        end = play_again(winner)
        if end == 'end':
            return 0
    
    print('\nNext round!')
    best_of_five()

def main():
    time.sleep(0.7)
    print(f'\nHowdy, {NAME}! Welcome to Rock, Paper, Scissors -- Cowboy Edition!\n')
    time.sleep(1)
    print(f'Ol\' {COMPUTER} is the meanest, most mustachioed machine this side of the net,\n'
          'and he\'s itchin\' for a showdown with you.\n'
    )
    time.sleep(1)
    print('Best of 5, Rock, Paper, Scissors, Lizard, Spock!\n'
          'Time to see who\'s the sharpest shot in town!\n'
    )
    time.sleep(1)

    see = see_instructions()
    if see:
        display_instructions()
    
    best_of_five()
    

main()
