# 1
# name = input('What is your name? ')
# sentence = 'Hello %s' % name
# print(sentence)

# 2
# name = input('What is your name? ')
# length_of_name = len(name)
# sentence = 'Hello %s! Your name has %d letters in it! Awesome!' % (
#     name, length_of_name)
# print(sentence.upper())

# 3
# name = input('What is your name? ')
# subject = input('What is your favorite subject? ')
# sentence = '%s\'s favorite subject in school is %s' % (name, subject)
# print(sentence)

# 4
# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sunday')
# elif day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# else:
#     print('Saturday')

# 5
# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sleep in')
# elif day == 1:
#     print('Go to work')
# elif day == 2:
#     print('Go to work')
# elif day == 3:
#     print('Go to work')
# elif day == 4:
#     print('Go to work')
# elif day == 5:
#     print('Go to work')
# else:
#     print('Sleep in')

# 6
# celsius = int(input('Temperature in C? '))
# conversion_to_fahrenheit = celsius * 1.8 + 32
# print(conversion_to_fahrenheit)

# 7
# bill_amount = int(input('Total bill amount? '))
# level_of_service = input('Level of service? ')

# if level_of_service == 'good':
#     tip_amount = bill_amount * .2
# elif level_of_service == 'fair':
#     tip_amount = bill_amount * .15
# else:
#     tip_amount = bill_amount * .10

# print('Tip amount: ' + str(tip_amount))
# print('Total amount: ' + str(tip_amount + bill_amount))

# 8
# bill_amount = int(input('Total bill amount? '))
# level_of_service = input('Level of service? ')
# number_of_people = int(input('Split how many ways? '))

# if level_of_service == 'good':
#     tip_amount = bill_amount * .2
# elif level_of_service == 'fair':
#     tip_amount = bill_amount * .15
# else:
#     tip_amount = bill_amount * .10

# print('Tip amount: ' + str(tip_amount))
# print('Total amount: ' + str(tip_amount + bill_amount))
# print('Amount per person: ' + str((tip_amount + bill_amount) / number_of_people))

# 9
# count = 0

# while count < 10:
#     count += 1
#     print(count)

# 10
# inital_coins = 0
# want_a_coin = input('Do you want a coin? ')
# while want_a_coin == 'yes':
#     inital_coins += 1
#     sentence = ('You have %d coins') % inital_coins
#     print(sentence)
#     want_a_coin = input('Do you want a coin? ')
# print('Bye')
