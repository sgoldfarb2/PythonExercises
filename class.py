#Class 2 - Python

#print('hello world')

#another way to print is to use sys and use sys.stdout.write
# import sys
# sys.stdout.write("hello world\n")

#let's talk about variables
# name = 'Sabrina'
# print(name)

#math using python
# found_coins = 15
# magic_coins = 20
# total_coins = found_coins + magic_coins
# print(total_coins)

#concatenation with python
# first_name = 'Sabrina'
# last_name = 'Goldfarb'
# name = first_name + ' ' + last_name
# print(name)

#using variables as aliases (%s %r %d)
# name = 'sabrina'
# age = 29
# sentence = '%s is %d years old' % (name, age)
# print(sentence)
#%s is for strings, %d is for integers (digits)

#string formatting - another way, equally useable as the %s and %d
# first_name = 'Sabrina'
# last_name = 'Goldfarb'
# # # sentence = 'Hello {} {}'.format(first_name, last_name)
# # # print(sentence)
# # #if you want to specifiy the position of the argument list, you can do that too
# # sentence = 'Hello {0} {1}'.format(first_name, last_name)
# # print(sentence)
# #you can also give your arguments an alias (see below)
# sentence = 'Hello {first} {last}'.format(first=first_name, last=last_name)
# print(sentence)
#any of these above methods are acceptable as well to reference your variables

#you can make paragraphs in python with triple quotes instead of having to use line breaks all the time

#input()
# name = input('What is your name? ')
# sentence = 'The user\'s name is %s' % name
# print(sentence)
#the user input is saved as the variable name
# birth_year = input('What is your year of birth? ')
# current_year = 2019
# age = current_year - int(birth_year)
# print(age)
#since we get input as a string, we need to use int() to make it an integer to do our math with it

#if statements in python
#if syntax for python is:
#if age >= 21:
#print('You get free beer')
