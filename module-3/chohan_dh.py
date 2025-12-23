"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

Module 3 changes by D'Jon Harrison:
- Input prompt changed to dh:
- House percentage changed to 12 percent
- Added bonus notice in introduction
- Added 10 mon bonus for dice totals of 2 or 7
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Bonus Notice:
If the dice total is 2 or 7, you receive a 10 mon bonus.
''')

purse = 5000

while True:  # Main game loop

    # Place bet
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('dh: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the dice.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Get CHO or HAN
    while True:
        bet = input('dh: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    # Reveal dice
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine result
    roll_is_even = (total % 2 == 0)
    correct_bet = 'CHO' if roll_is_even else 'HAN'
    player_won = (bet == correct_bet)

    # Win or lose
    if player_won:
        print('You won! You take', pot, 'mon.')
        purse += pot

        house_fee = (pot * 12) // 100  # 12 percent house cut
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    # Bonus check
    if total == 2 or total == 7:
        print('Bonus! You rolled a total of', total, 'and earned 10 mon.')
        purse += 10

    # Out of money check
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
