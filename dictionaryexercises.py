# #1

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# #1.1
# print(phonebook_dict['Elizabeth'])

# #1.2
# phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict)

# #1.3
# del phonebook_dict['Alice']
# print(phonebook_dict)

# #1.4
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict['Bob'])

# #1.5
# print(phonebook_dict.values())



# #2
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#      {
#        'name': 'Jasmine',
#        'email': 'jasmine@yahoo.com',
#        'interests': ['photography', 'tennis']
#      },
#      {
#         'name': 'Jan',
#         'email': 'jan@hotmail.com',
#         'interests': ['movies', 'tv']
#      }
#     ]
# }

# #2.1
# ramit_email = ramit['email']
# print(ramit_email)

# #2.2
# ramits_first_interest = ramit['interests'][0]
# print(ramits_first_interest)

# #2.3
# jasmines_email = ramit['friends'][0]['email']
# print(jasmines_email)

# #2.4
# jans_second_interest = ramit['friends'][1]['interests'][1]
# print(jans_second_interest)


# #3
# dict_of_letters = {}
# def letter_histogram():
#
#   word = input('Give me a word, any word! ')
#   for letter in word:
#     if(dict_of_letters.get(letter) != None):
#       dict_of_letters[letter] = dict_of_letters[letter] + 1
#     else:
#       dict_of_letters[letter] = 1
#   print(dict_of_letters)
#   return dict_of_letters


# letter_histogram()


# #4
dict_of_words = {}
def word_histogram():

  paragraph = input('Type in a paragraph please! ')
  list_of_words = paragraph.split()
  for i in list_of_words:
    if(dict_of_words.get(i) != None):
      dict_of_words[i] = dict_of_words[i] + 1
    else:
      dict_of_words[i] = 1
  print(dict_of_words)
  return dict_of_words


word_histogram()


#BONUS!!
#given a tally from #3 or #4, print the top three words or letters
# def histogram_tally(our_dict):
#   our_numbers = []
#   greatest_value = []
#   for key in our_dict:
#     our_numbers.append(our_dict[key])
#   print(our_numbers)
#   for i in our_numbers:
#     if(our_numbers[i] < our_numbers[i+1]):
#       greatest_value.append(our_numbers[i+1])
#   print(greatest_value)
#   for key, value in our_dict.items():
#     if value == search_value:
#       print(key)

# histogram_tally(dict_of_words)

