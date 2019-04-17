# step 1
# secret_number = 5
# player_guess = int(input('Guess a number: '))

# while (player_guess != secret_number):
#     print('Nope, try again')
#     player_guess = int(input('Whats the number? '))
# print('Yes! You win!')

# step 2
# secret_number = 5
# player_guess = int(input('Guess a number: '))

# while (player_guess != secret_number):
#     if (player_guess < secret_number):
#         player_guess = int(input('Your guess is too low! Whats the number? '))
#     else:
#         player_guess = int(input('Your guess is too high! Whats the number? '))
# print('Yes! You win!')


# step 3
# import random
# secret_number = random.randint(1, 10)
# player_guess = int(input('Guess a number: '))

# while (player_guess != secret_number):
#     if (player_guess < secret_number):
#         player_guess = int(input('Your guess is too low! Whats the number? '))
#     else:
#         player_guess = int(input('Your guess is too high! Whats the number? '))
# print('Yes! You win!')


# step 4
# import random
# secret_number = random.randint(1, 10)
# player_guess = int(input('Guess a number: '))
# guesses_remaining = 4
# while (player_guess != secret_number):
#     guesses_remaining -= 1
#     if (player_guess < secret_number and guesses_remaining > 0):
#         player_guess = int(
#             input('Your guess is too low! Whats the number? '))
#     elif (player_guess > secret_number and guesses_remaining > 0):
#         player_guess = int(
#             input('Your guess is too high! Whats the number? '))
#     elif (player_guess < secret_number and guesses_remaining == 0):
#         print('Sorry, your number is too low and you ran out of guesses!')
#         break
#     else:
#         print('Sorry, your guess is too high and you ran out of guesses!')
#         break
# if(player_guess == secret_number):
#     print('Yes, you win!')


# step 5
import random
secret_number = random.randint(1, 10)
player_guess = int(input('Guess a number: '))
guesses_remaining = 5
while (player_guess != secret_number):
    guesses_remaining -= 1
    if (player_guess < secret_number and guesses_remaining > 0):
        player_guess = int(
            input(f'Your guess is too low! You have {guesses_remaining} guesses left. Whats the number? '))
    elif (player_guess > secret_number and guesses_remaining > 0):
        player_guess = int(
            input(f'Your guess is too high! You have {guesses_remaining} guesses left. Whats the number? '))
    elif (player_guess < secret_number and guesses_remaining == 0):
        print('Sorry, your number is too low and you ran out of guesses!')
        play_again = input('Do you want to play again? Y or N? ')
        if (play_again == 'Y'):
            secret_number = random.randint(1, 10)
            guesses_remaining = 4
        else:
            print('Bye!')
        break
    else:
        print('Sorry, your guess is too high and you ran out of guesses!')
        play_again = input('Do you want to play again? Y or N? ')
        if (play_again == 'Y'):
            secret_number = random.randint(1, 10)
            guesses_remaining = 4
        else:
            print('Bye!')
        break
if(player_guess == secret_number):
    print('Yes, you win!')
    play_again = input('Do you want to play again? Y or N? ')
    if (play_again == 'Y'):
        secret_number = random.randint(1, 10)
        guesses_remaining = 4
    else:
        print('Bye!')

# still need to make it reset and start the game over, but all other functionality is working
