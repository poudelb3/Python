## OOP

class PlayerCharacter:
    # Class Object Attribute, 
    membership = True
    # Class Object attributes, membership is accessible anywhere in 
    # the class by ' self. ' or ' PlayerCharacter. '
    # it doesn't change in the class
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name #attributes, 
            #self refers to object, in this case, player1 and player2
            # these attributes are dynamic, it can change
            self.age = age
    
    def shout(self):
        print(f'My name is {self.name}')
        # must use the " self. " to access name parameter here

player1 = PlayerCharacter('Cindy', 34)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.shout())
