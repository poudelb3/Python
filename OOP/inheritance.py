# INHERITANCE

'''
Here, Wizard && Archer are inherited from Parent Class -- User --
-> Wizard && Archer share some part of the USER, but
-> They also have different methods, & properties that they need

'''

class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'{self.name} attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} attacking with arrows: arrows left {self.num_arrows}')

wizard1 = Wizard('Mervin', 50)
archer1 = Archer('Robin', 100)

archer1.sign_in(); wizard1.sign_in()
archer1.attack()
wizard1.attack()

## Check if sth is an INSTANCE of a Class
print(isinstance(wizard1, Wizard)) # returns True since wizard1 is an object of Wizard

'''
Polymorphism
-> allows to use the same methods in different forms
'''
print("------------ Polymorphism ---------------")
# Below, calling same method outputs different depending on which 
# child class object is calling it
for char in [wizard1, archer1]:
    char.attack()
