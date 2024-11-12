class Dog:
    def __init__(self, name, age, weight, breed):
        self.name = name 
        self.age = age 
        self.weight = weight
        self.breed = breed

    def print_dog(self):
        print(f"{self.name} is a {self.breed}.It is {self.age} years old. It weighs {self.weight} kg.")

    def human_years(self):
        print(f"{self.name} is {self.age*7} years old in human years")

class HuntingDog(Dog):
    def __init__(self,name, age,weight,breed, handler):
        Dog.__init__(self, name, age,weight, breed)
        self.handler = handler
    def hunting(self):
        print(f"{self.name} is a hunting dog. it helps {self.handler} to hunt bush meat.")
    

class BullDog(Dog):
    def __init__(self,name, age,weight,breed, killing):
        Dog.__init__(self, name, age,weight, breed)
        self.killer = killing
    def hunting(self):
        print(f"{self.name} is a bulldog. it helps {self.killer} to hunt bush meat.")

class GtaDog(Dog):
    def __init__(self,name, age, weight, breed, game):
        Dog.__init__(self,name ,age,weight,breed)
        self.game = game
    def Gta(self):
        print(f"{Ripper.name} he is a demon dog that loves to eat people alive😈. He loves to see the terror in the peoples eyes when his about to feed on his victims😨")






bingo = Dog('Bax',12,40, 'Bax')
# bax.print_dog()
# bax.human_years()
Ripper = GtaDog('Ripper',5,45,'Ripper','He')
Ripper.print_dog()
Ripper.human_years()
Ripper.Gta()
print(f"{Ripper.name} has more rage than {bingo.name}. Bacause {bingo.breed} is a bitch and {Ripper.breed} is a beast😈")


