secret_number = 5
player_guess = int(input('Guess a number: '))

while (player_guess != secret_number):
    print('Nope, try again')
    player_guess = int(input('Whats the number? '))
print('Yes! You win!')
