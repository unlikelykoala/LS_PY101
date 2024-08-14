import json
import random
import time
from os import system
import cowsay
from tabulate import tabulate

# Open the json file for reading
with open('refactored_messages.json', 'r') as file:
    MESSAGES = json.load(file)

system('clear')

player = 'rock'
print('lizard' in MESSAGES['verb'][player].keys())
