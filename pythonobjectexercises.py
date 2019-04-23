#1

class Person:
  def __init__(self, name, email, phone):
     self.name = name
     self.email = email
     self.phone = phone
     self.friends = []
     self.greeting_count = 0
     self.people_greeted = []

  def greet(self, other_person):
    self.greeting_count = self.greeting_count + 1
    if other_person not in self.people_greeted:
     self.people_greeted.append(other_person)
    print(self.greeting_count)
    print('Hello {}, I am {}!'.format(other_person.name, self.name))

  def print_contact_info(self):
    print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

  def add_friend(self, name):
    self.friends.append(name)
    print(self.friends)

  def num_friends(self):
    print(len(self.friends))
    return len(self.friends)

  def __str__(self):
    return f'Person: {self.name} {self.email} {self.phone}'

  def num_unique_people_greeted(self):
    print(len(self.people_greeted))



#1.1
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
#1.2
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#1.3
sonny.greet(jordan)
#1.4
jordan.greet(sonny)
#1.5
print(f'Jordan\'s number is {jordan.phone} and Jordan\s email is {jordan.email}')
#1.6
print(f'Sonny\'s number is {jordan.phone} and Sonny\s email is {jordan.email}')

#still need to do the bonus

jordan.greet(sonny)
jordan.greet(sonny)

jordan.num_unique_people_greeted()


#2
class Vehicle:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def print_info(self):
    print(f'{self.year} {self.make} {self.model}')
