#Dictionaries
#same as objects in JS - key/value pairs
#dictionary_name = {
#   key : value,
#   key2 : value2
# }

#to access values in a dictionary
#dictionary_name[key]

#get method
#use the get() method to safely retrieve items where you're not sure if the key exists
#it will return None if the key is not in the dictionary

#example:
#my_dictionary = {
#   'hi': 'world',
#   1 : 2,
#   'dictionary': 'woohoo'
# }
#result = my_dictionary.get('student') -> None
#if it is there, will return the value associated with that key

#in
#use the in operator to check if a key is in a dictionary

#example:
#is_it_there = 'student' in my_dictionary
#print(is_it_there) -> will return False
#if it is there, will return True
#can be used IN your if statement since it evaluates to true or false

#example:
#if "hi" is in my dictionary:
# print("found!")
#else:
# print("not found :(")

#adding new values
#my_dictionary["new_key"] = "new_value"

#dictionaries are mutable so you can change a key/value pair the same way

#keys() allows you to get all of the keys of the dictionary
#values() gets all of the values in a dictionary
#will give you the result in a sequence (like a list)!

#example of accessing the keys
# my_dictionary = {
#   'hi': 'world',
#   1 : 2,
#   'dictionary': 'woohoo'
# }
# results = my_dictionary.keys()
# print(results)
# for result in results:
#   print(result)

#example of accessing the values
# my_dictionary = {
#   'hi': 'world',
#   1 : 2,
#   'dictionary': 'woohoo'
# }
# results = my_dictionary.values()
# print(results)
# for result in results:
#   print(result)

#del && items()
#del deletes an item from a dictionary && items() is an alternate way of getting entries
#an entry is a tuple containing the key and value for every pair in the dictionary

#del example:
# my_dictionary = {
#   'hi': 'world',
#   1 : 2,
#   'dictionary': 'woohoo'
# }
# del my_dictionary[1]
# print(my_dictionary)

#items() example
# my_dictionary = {
#   'hi': 'world',
#   1 : 2,
#   'dictionary': 'woohoo'
# }
# items = my_dictionary.items()
# print(items)
# #to iterate through the sequence that returns from items:
# for key, value in my_dictionary.items():
#   print(f'my key is {key} is and my value is {value}')

#nesting
# contact = [
#     {
#         'first_name': 'Phillip',
#         'last_name': 'Guo',
#         'email': 'phillip.guo@gmail.com',
#         'phone':{
#             'work':'837-494-3948',
#             'cell': '234-897-4933'
#         }
#     },
#     {
#         'first_name': 'Mark',
#         'last_name': 'Guzdial',
#         'email': 'mark.guzdial@gatech.edu',
#         'phone':{
#             'work':'484-569-3466',
#             'cell': '493-485-9845'
#         }
#     }
# ]

#to access Phillip's email
# print(contact[0]['email'])

#to access Mark's cell number
# print(contact[1]['phone']['cell'])


#Errors

#give your programs an if where if a certain block of code fails, something else will happen instead of someone who can't code getting stuck somewhere

#error handling
# while True:
#   try:
#     x = int(input('Please enter a number: '))
#  #in case someone puts something other than a valid number in, we need an exception so our program doesn't break
#     break;
#   except ValueError:
#     print('Oops! That wasn\'t a valid number. Try again!')

#try is a keyword, where you are seeing if something fails

#try to catch specific errors instead of all errors as a whole, use the specific error exceptions!!

#you wont usually use finally in python, it will ALWAYS execute, so you usually put cleanup information in it

#you can create your own errors
#use the keyword raise to create your own exception

# x = 10
# if x > 5:
#   raise Exception('this is a custom error because x should not be greater than 5')

  #exceptions will go back to a file and log the exceptions, so you can go back later and fix things



#Pickling to save your information into a file
#to save the data
# import pickle

# my_dictionary = {'name' : 'sabrina'}

# with open('my_dictionary.pickle', 'wb') as fh:
#   pickle.dump(my_dictionary, fh)

#to open the data
# import pickle

# with open('my_dictionary.pickle', 'rb') as fh:
#   my_dictionary = pickle.load(fh)
#   print(my_dictionary)

# print(my_dictionary['name'])
