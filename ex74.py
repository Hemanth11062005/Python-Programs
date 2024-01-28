#multiple inheritance
class Prey:
    def __init__(self,animal):
        self.animal = animal
        
        
    def flee(self):
        print(self.animal+" animal flees")
        
class Predator:
    def __init__(self,animal):
        self.animal = animal
    
    def hunt(self):
        print(self.animal+" animal hunts")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabbit = Rabbit("Bunny")
hawk = Hawk("Hawkay")
fish = Fish("Jelly")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
        