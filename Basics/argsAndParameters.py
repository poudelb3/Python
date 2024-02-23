'''
Parameters 
-> are used when defining a function
'''

def say_hello(name, emoji):
    print(f"hellllooooo {name} {emoji}")


'''
Arguments
-> these are the values given to function parameters
-> are used when calling/invoking a function
-> Postional arguments: the positions of arguments matter on how the function behaves
'''

say_hello('Andrei', '😊')
say_hello('Leiza', '😊')
say_hello('Brandon', '😊')


'''
Keyword Arguments
-> does not matter the order/position of arguments in the function
-> this is not a good practice, Stick to the way function is defined
'''
# here, even though the two args are in different order, the function
# behaves as expected
say_hello(emoji='😊', name="Bibi")