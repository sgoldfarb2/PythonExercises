# Day 3
# creating a list
# variable_name = []
# my_list = ['Monday', 'Tuesday']
# index starts at 0
# my_list[0]


# using len to get length
# num = len(my_list) will give you the integer of how many elements you have in your list

# using append
# second_list = [1, 2, 3]
# my_list.append('second_list')

# list slicing
# works on lists, strings, tuples, and objects
# in python, you slice with [x:y] where it includes index x, and doesn't include index y
# if you want to start at the beginning or end at the end, you don't need x or y for example [:3] or [3:]

# list methods
# list.insert(index, item) - inserts item at a specific location
# list.extend([3, 4, 5]) - appends a list to the original list
# list.pop() - removes the last item in the list
# list.index(item) - gives you the index of that item
# list.sort() - sorts a list
# list.copy() - creates a new copy of a list
# list.clear() - removes all items from a list

# in python (as in JS), lists/objects/functions are pass by reference, not pass by value

# strings are just like lists and can use list methods
# str = 'Hello'
# str[0] -> 'H'
# str[1:3] -> 'el'
# len(str) -> 5

# list operators
# concatenate is done using a + symbol
# concatenate with self multiple times (list * 3)

# multi-dimensional arrays
# works the same as JS, where your index is grabbing the elements even if it's an array
# example:
# my_list = [[1, 2], [2, 3], [3, 4]]
# print(my_list[2])   -> [3,4]
# print(my_list[2][0])   -> 3

# tuples
# tuples are immutatble
# just like lists, except they are immutable
# tuples are made with parenthesis
# my_tuple = (1, 2, 'Fred', [1, 2])
# print(my_tuple[3])
# parenthesis are optional, but it helps programmers understand you are using a tuple, so always use them
# one, two, three = (1, 2, 3) -> this is called destructuring which you can also do in JS
# print(one) -> 1
# print(two) -> 2
# print(three) -> 3
# destructuring will assign the first variable name to the first index, second to the second index, etc

# while loopd
# while(condition):
#   print a

# range
# range(start, upto, step)
# start and step are both optional
# upto is where it ends, not including that upto value

# for loops
# different than in JS
# acts more like a forEach in JS
# for item in variable:
#  print item

# for loops with ranges
# for number in range(0, 10):
#   print number

# nested for loops
# for num in range(10):
#     print(num)
#     for inner in range(10):
#         print(inner)

# # create a multiplication table from 0 to 10
# for num in range(1, 10):
#     for inner in range(10):
#         print(("%d x %d = %d") % (num, inner, num * inner))

# another way to print with formatting
# print(f"{num} x {inner} = {result}")
