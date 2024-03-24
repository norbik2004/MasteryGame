import random
from typing import List

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10


def generate_random_colors() -> List[str]:
    random_colors = []
    for _ in range(4):
        random_colors.append(COLORS[random.randint(0, len(COLORS) - 1)])
    return random_colors


def game():
    tries = TRIES
    colors = generate_random_colors()
    print("Welcome to Mastery Game!")
    print(f'You have {TRIES} tries to guess randomnly generated colours')
    print(f'You can choose from {COLORS}')
    while tries > 0:
        good_colors = check_colours(player_input(), colors)
        tries -= 1
        print(f'You have {tries} tries, u guessed {good_colors} You can choose from {COLORS}')
        if good_colors == 4:
            print("You won!")
            break

    else:
        print("You lost! CYA BBY")
        print("it was " + str(colors))


def player_input() -> List[str]:
    colours_input = input("Enter your colours: MAX 4 characters \n")
    while len(colours_input) != 4:
        print("Please enter 4 characters")
        colours_input = input("Enter your colours: MAX 4 characters \n")
    player_input_list = list(colours_input)
    return player_input_list


def check_colours(player_colours_input, random_colors) -> int:
    good = 0
    for i in range(len(player_colours_input)):
        if player_colours_input[i].upper() == random_colors[i].upper():
            good += 1
    return good

