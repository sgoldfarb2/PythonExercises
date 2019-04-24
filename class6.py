#Classes continued

#Inheritance vs. Composition
#inheritance is having something your children classes can reuse
#which is better? there's a debate
#composition would be if you had a 'master' class that contains the objects made from another class
#this is a way to manage the objects made from your class, so they aren't loose separate objects

#an example of composition:
#school is going to be our management system class, students will be our class that makes our student objects
# class Student:
#   def __init__(self, first_name, last_name, location):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.location = location

#   def print_student_name(self):
#     print(f'{self.first_name} {self.last_name} is at our {self.location} campus')

#with composition, you create another class which creates these objects for you
# sabrina = Student('Sabrina', 'Goldfarb', 'Houston')
# alfie = Student('Alfie', 'Santos', 'Houston')
# michael = Student('Michael', 'Dao', 'Houston')
# cindy = Student('Cindy', 'Crawford', 'Atlanta')

# class Campus:
#   def __init__(self):
#     self.all_students = []

#   def add_new_student(self, first_name, last_name, location):
#     temp = Student(first_name, last_name, location)
#     self.all_students.append(temp)

#   def see_all_students(self):
#     for student in self.all_students:
#       print(f'{student.first_name} {student.last_name} at our campus in {student.location}')


# management_tool = Campus()

# management_tool.add_new_student('Sabrina', 'Goldfarb', 'Houston')
# management_tool.add_new_student('Alfie', 'Santos', 'Houston')
# management_tool.add_new_student('Michael', 'Dao', 'Houston')
# management_tool.add_new_student('Cindy', 'Crawford', 'Atlanta')
# management_tool.see_all_students()


