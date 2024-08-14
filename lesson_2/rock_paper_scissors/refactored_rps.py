import json
from os import system
import random
import sys
import time
import cowsay
from tabulate import tabulate

# Open the json file for reading
with open('refactored_messages.json', 'r') as file:
    MESSAGES = json.load(file)

system('clear')

# initialize constants
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
WIN_NUMBER = 3

def get_player_name():
    player = input(MESSAGES['get_name']['1'])
    while not player:
        player = input(MESSAGES['get_name']['2'])
    return player

def get_computer_name():
    computer = MESSAGES['computer_name'][random.choice(['1', '2', '3', '4'])]
    return computer

def init_scores(player, computer):
    return {
    player : 0,
    computer : 0,
    'Tie' : 0
}

def keep_going():
    input(MESSAGES['keep_going'])
    print("\033[A\033[K", end="")

def keep_going_clear():
    input(MESSAGES['keep_going'])
    system('clear')

def intro(player, computer):
    welcome1 = MESSAGES['intro']['1'].format(player=player)
    welcome2 = MESSAGES['intro']['2'].format(computer=computer)
    welcome3 = MESSAGES['intro']['3']

    print(welcome1)
    keep_going()

    print(welcome2)
    keep_going()

    print(welcome3)
    keep_going()

def display_rules():
    system('clear')
    for win_tool, dict_ in MESSAGES['verb'].items():
        for lose_tool, action in dict_.items():
            print(f'--{win_tool} {action} {lose_tool}')
    keep_going_clear()

def request_rules():
    response = input(MESSAGES['rules']['see'])
    while response.casefold() not in ['y', 'n']:
        response = input(MESSAGES['rules']['error'])

    if response.casefold() == 'y':
        system('clear')
        display_rules()
    else:
        system('clear')

def is_invalid(choice_):

    try:
        int_choice = int(choice_)
        if int_choice not in range(1, 7):
            return True
    except (TypeError, ValueError):
        return True
    return False

def display_choice_list():
    choices = VALID_CHOICES + ['See rules']
    for index, weapon in enumerate(choices, start=1):
        print(f'{index}. {weapon}', sep=', ')

def get_player_choice():
    system('clear')

    while True:
        print(MESSAGES['player_choice']['1'])
        display_choice_list()
        choice = input(MESSAGES['player_choice']['2'])
        print()

        while is_invalid(choice):
            print(MESSAGES['error'][random.choice(['1', '2', '3', '4'])])
            choice = input(MESSAGES['player_choice']['2'])

        if choice == '6':
            display_rules()
        else:
            time.sleep(0.2)
            return VALID_CHOICES[int(choice) - 1]

def get_winner_and_winmove_losemove(player, computer, \
                                    player_move, computer_move):
    if player_move == computer_move:
        return 'Tie', player_move, computer_move

    # player wins
    if computer_move in MESSAGES['verb'][player_move].keys():
        return player, player_move, computer_move

    # computer wins
    return computer, computer_move, player_move

def countdown():
    system('clear')
    count = list(range(3, 0, -1))
    for n in count:
        print(f'{n}... ', end='', flush=True)
        time.sleep(0.7)
    print(MESSAGES['countdown'])
    time.sleep(0.4)

def display_winner(champ, win_choice, lose_choice):
    if champ == 'Tie':
        print(MESSAGES['disp_winner']['tie']['1'])
        print(MESSAGES['disp_winner']['tie']['2']\
              .format(win_choice=win_choice, lose_choice=lose_choice))
    else:
        print(f'{win_choice.title()} '
              f'{MESSAGES['verb'][win_choice][lose_choice]} '
                f'{lose_choice}!')
        print(MESSAGES['disp_winner']['else'].format(champ=champ))
    keep_going_clear()

def update_score(scoreboard, champ):
    scoreboard[champ] += 1

def display_scores(scoreboard):
    score_lst = [[key, value] for key, value in scoreboard.items()]
    print(tabulate(score_lst, headers=['', 'Score'], tablefmt="heavy_grid"))
    keep_going_clear()

def game_over(scoreboard, champ):
    if scoreboard[champ] == 3 and champ != 'Tie':
        return True
    return False

def gameover_message(champ, player, computer):
    system('clear')
    if champ == player:
        print(f"{MESSAGES['game_over']['player_wins']['1']}")
        time.sleep(0.5)
        print(MESSAGES['game_over']['player_wins']['2']\
              .format(computer=computer))
    else:
        print(MESSAGES['game_over']['pc_wins']['1'].format(player=player))
        time.sleep(0.5)
        print(MESSAGES['game_over']['pc_wins']['2'].format(computer=computer))

def play_again():
    response = input(MESSAGES['play_again']['1'])
    while response.casefold() not in['y', 'n']:
        print(MESSAGES['error'][random.choice(['1', '2', '3', '4'])])
        response = input(MESSAGES['play_again']['1'])

    if response.casefold() == 'y':
        system('clear')
        main()
    else:
        system('clear')
        cowsay.cow(MESSAGES['play_again']['2'])
        sys.exit()

def best_of_five(player, computer, scoreboard):
    player_choice = get_player_choice()

    computer_choice = random.choice(VALID_CHOICES)

    winner, win_tool, lose_tool = \
        get_winner_and_winmove_losemove(player, computer, \
                                        player_choice, computer_choice)
    countdown()
    display_winner(winner, win_tool, lose_tool)

    update_score(scoreboard, winner)
    display_scores(scoreboard)

    if game_over(scoreboard, winner):
        gameover_message(winner, player, computer)
        play_again()


    print('\nNext round!')
    best_of_five(player, computer, scoreboard)

def main():
    player_name = get_player_name()
    computer_name = get_computer_name()
    scores = init_scores(player_name, computer_name)

    intro(player_name, computer_name)
    request_rules()

    best_of_five(player_name, computer_name, scores)


main()
