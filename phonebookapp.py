#write a phone book app!

phone_book = {
'sabrina': 111
}


def electronic_phone_book():
  print("""
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")
  thing_to_do = int(input('What do you want to do? (1-5) '))

  while thing_to_do <= 5:
    if thing_to_do == 1 :
      who_to_look_up = input('Who do you want to look up? ')
      print(phone_book[who_to_look_up])
      thing_to_do = int(input('What do you want to do? (1-5) '))
    elif thing_to_do == 2:
      their_name = input('What is their name? ')
      their_number = input('What is their number? ')
      phone_book[their_name] = their_number
      thing_to_do = int(input('What do you want to do? (1-5) '))
    elif thing_to_do == 3:
      who_to_delete = input('Who do you want to delete? ')
      del phone_book[who_to_delete]
      thing_to_do = int(input('What do you want to do? (1-5) '))
    elif thing_to_do == 4:
      print(phone_book)
      thing_to_do = int(input('What do you want to do? (1-5) '))
    else:
      print('Bye!')
      break

electronic_phone_book()
