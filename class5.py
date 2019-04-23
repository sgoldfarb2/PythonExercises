#Object Oriented Programming


#Classes!
#Similar to classes in JS! Yay!
#in python, you set classes like this:
#class ClassName:
  #properties
  #functions

# class Students:


# #self differentiates each instance from each other
#   def print_students(self):
#     print(f'we have students!')

# # #same as JS, to call the methods within the classes
# # Students.print_students()

# Michael = Students() #Michael is an instance of Students
# Michael.print_students() #this is us running our print_students method using our Michael instance

# Chris = Students()
# Chris.print_students()

#working with constructors ( def __init__(self): )
# class Students:
#   def __init__(self):
#     pass
#init INITIALIZES the variables in our class
#Michael = Students()

#now let's add some things to our class to create our instance objects!
# class Students:
#   def __init__(self, name, surname, birthdate):
#     self.name = name
#     self.surname = surname
#     self.birthdate = birthdate

# Michael = Students('Michael', 'Dao', 'March 3')

#lastly, we need to start defining methods with our objects!
# import datetime

# class Students:
#   def __init__(self, name, surname, birthdate):
#     self.name = name
#     self.surname = surname
#     self.birthdate = birthdate
#   def print_name(self):
#     return f'My name is {self.name}'

# Michael = Students('Michael', 'Dao', 1990)
# print(Michael.print_name())

#more practice with classes!
# class Person:
#   def __init__(self, name):
#     self.name = name
#     self.count = 0
#     print(f'{self.name} and count {self.count}')
#   def change_name(self, new_name):
#     self.name = new_name
#     self.count = self.count + 1
#     print(f'{self.name} and count {self.count}')

# student = Person('Veronica')
# student.change_name('Matt')
# student.change_name('Sabrina')


#Another example, using phones/types and turning them on/off
# class Phone:
#   def __init__(self, phone_type):
#     self.phone_type = phone_type
#     self.isOn = "off"
#   def print_type(self):
#     print(f'This phone is an {self.phone_type}')
#   def turn_on(self):
#     print('You turned your phone on!')
#     self.isOn = 'on'
#   def turn_off(self):
#     print('You turned your phone off!')
#     self.isOn = 'off'
#   def is_it_on(self):
#     print(f'your phone is an {self.phone_type} and it is currently {self.isOn}')

# apple = Phone('apple')
# apple.print_type()
# android = Phone('android')
# android.print_type()
# blackberry = Phone('blackberry')
# blackberry.print_type()
# apple.turn_on()
# apple.is_it_on()
# apple.turn_off
# blackberry.is_it_on()
# android.turn_on()
# android.turn_off()
# android.is_it_on()


#Another example using cars
# class Car:
#   def __init__(self, make, model, color):
#     self.make = make
#     self.model = model
#     self.color = color
#     self.door_status = 'closed'
#     print(f'Nice {self.make} {self.model} in {self.color}')

#   def change_color(self, new_color):
#     self.color = new_color

#   def open_door(self):
#     self.door_status = 'open'

#   def display_color(self):
#     print(f'the color of your {self.make} {self.model} is {self.color}')

#   def display_info(self):
#     return f'Nice {self.make} {self.model} in {self.color}'

# toyota = Car('toyota', 'prius', 'green')
# honda = Car('honda', 'crv', 'purple')
# hyundai = Car('hyundai', 'tucson', 'blue')
# toyota.display_color()
# toyota.change_color('red')
# toyota.display_color()

# #say we want to see all of our cars information at once, we can create a list of objects with our instances!
# fleet = [toyota, honda, hyundai]
# for vehicle in fleet:
#   print(vehicle.display_info())


