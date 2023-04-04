import random

sides = int(input('how many sides does your dice have? '))

random_integer = random.randint(1,sides)

print('you rolled a {}'.format(random_integer))


def flip_coin():
    random_number = random.randint(1,2)
    if random_number == 1:
        side = 'heads'

    else:
        side = 'tails'

    return side

choice = input('heads or tails: ')
result = flip_coin()

print('the coin landed on {}'. format(result))

if choice == result:
    print('Congratulation! The user won the game')
else:
    print('You lost sucker!!')


def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'

    return choice

my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
if my_choice == 'rock' and opponent_choice == 'paper':
    print('You lose!')
if my_choice == 'paper' and opponent_choice == 'rock':
    print('You win!')
if my_choice == 'scissors' and opponent_choice == 'rock':
    print('You lose!')
if my_choice == 'rock' and opponent_choice == 'rock':
    print('try again!')
if my_choice == 'scissors' and opponent_choice == 'scissors':
    print('try again!')
if my_choice == 'paper' and opponent_choice == 'paper':
    print('try again!')
if my_choice == 'scissors' and opponent_choice == 'paper':
    print('You win!')
if my_choice == 'paper' and opponent_choice == 'scissors':
    print('You lose!')

