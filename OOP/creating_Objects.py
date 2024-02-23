## OOP

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes, 
        #self refers to object, in this case, player1 and player2
        self.age = age
    
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 34)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.age)
print(player2.attack)
print(player2.run())
