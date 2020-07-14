from pdb import set_trace as breakpoint


class Dog():
    def __init__(self, name, age, housebroke):
        self.name = name
        self.age = age
        self.housebroke = housebroke

    def is_housebroke(self):
        if self.housebroke == True:
            print(f'{self.name} is housebroken!')
        else:
            print(f'{self.name} is not housebroken... :(')


#class Beagle(Dog):
 #   def __init__(self, name, age, housebroke):
  #      self.name = name
   #     self.age = age
    #    self.housebroke = housebroke

    #def barks_alot(self, barker):
