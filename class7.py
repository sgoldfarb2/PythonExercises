class Character:
  def __init__(self, health, power):
    self.health = health
    self.power = power


class Hero(Character):
   #since we don't have any constructor in here, we are going to get our constructor variables from our parent class, the Character class
  #if you put a def __init__(self) in this class, you're going to override the character class, and the variables will no longer be set in the hero class
  #you need to use the super() function to make this work if you have a def __init__(self)
  def __init__(self):
    super(Hero, self).__init__(health, power)
    #this is how you'd make it work with the def init and taking the health and power from the Character class
    #this might be necessary if there are other things you need to initialize within the Hero class

class Goblin(Character):
  pass #this does the same thing. since goblin is inheriting from the Character class, we don't even need to have self.health = health and self.power = power!

