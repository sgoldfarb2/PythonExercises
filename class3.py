#functions in python
#reusable code that performs a specific task
#has three parts, a name, parameters, and a body -- parameters are optional
#declared differently than in JS, in python we declare functions like this
# def fun_name(our_parameter(s)):
#   body

# def get_groceries():
#   print('milk')
#   print('flour')
#   print('sugar')
#   print('butter')
#   print()

#   get_groceries()
#just like in JS, you need to call your function for it to run

#nested functions
# def separate_runs():
#   print('**********')
#   print()

# def get_groceries():
#   print('milk')
#   print('flour')
#   print('sugar')
#   print('butter')
#   separate_runs() -> calling the separate_runs function within our get_groceries function, so we get the stars in a line

# get_groceries() -> calls get_groceries, which calls separate_runs since it's called within get_groceries

# def blend(power, minutes):
#   print(power * minutes)

# for i in range(0, 10):
#   p = 2 * i
#   m = 3 * i
#   blend(p, m)
#ANSWERS
# 0
# 6
# 24
# 54
# 96
# 150
# 216
# 294
# 384
# 486
#in the above example, i will change each time and call the function each time so we will get all of the answers from the for loop run through the blend function

#returning in Python
#if you don't return anything, you return None

# def add_two(starting_value):
#   return starting_value + 2

# our_number = add_two(4)
# print(our_number)

# def square(n):
#   return n, n*n, 2*n

# variable1, variable2, variable3 = square(5)
#in the above function, we are returning multiple things, so we need to assign multiple variables to hold each of the things we return

#arguments need to be passed positionally, because the first arg will get assigned with the first space in the arguments
#if you call the arguments by name, the order of arguments doesn't matter
#example:
# from math import sqrt
# def quadratic(a, b, c):
#   x1 = -b / (2*a)
#   x2 = sqrt(b**2 - 4*a*c) / (2*a)
#   return (x1 + x2), (x1 - x2)

# print(quadratic(c=62, a=31, b=93))
#since we have declared our specific variables that are found within the function, it doesn't matter where we place our values

#print has a parameter called sep', ' which when used separates what's inside with a deliminator
# print('comma', 'separator', 'function', sep='*')

#return statements like in JS break you out of your function
# def hello_world():
#   print('hola')
#   return
#   print('hi') -> this will never print because our return statement broke us out of our function

# hello_world()

#scope and python!
# same as JS
#scope and lists in python
# my_list = [3, 7, 4, 9, 12]

# def something(a_list):
#   a_list[1] = 1990

# something(my_list)
# print(my_list)
#this will mutate the original list

#plotting








#turtle graphics
from turtle import *

#drawing a circle
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)

# mainloop()

# drawing a square again
# up()
# forward(50)
# left(90)
# forward(50)
# left(90)
# down()
# # draw the square
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# mainloop()

#draw a circle
# pencolor('orange')
# width(10)
# circle(180)

#draw a star
# for i in range(5):
#     forward(100)
#     right(144)
# mainloop()

