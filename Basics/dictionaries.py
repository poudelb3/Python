#Dictionaries

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'c': True
}

print(dictionary['a'][1]) #pirnts 2


'''
--> Dictionary KEYS has to be IMMUTABLE, usually a string
--> Keys has to be unique, & can be over-written if a key is defined again

'''

## Dictionary Methods
idk = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'c': True
}

print(idk.get('age')) # returns None if key doesn't exists instead of throwing an error

print(idk.get('age', 55)) # returns default value 55 if age doesn't exist


## Alternatively way of creating DICTIONARY
user = dict(name = "john doe", age = 50)
print(user)

print('basket' in idk) # prints True since 'basket exists in idk dict
print('user' in idk); # prinsts FALSE

# Getting Keys and Values
user1 = dict(basket = [1,2,3], greet = 'hello', age = 20)
print('hello' in user1.keys()) # returns false coz 'hello' is in values
print('hello' in user1.values()) # returns True

print(user.items()) # reurns all the items in dict

user2 = user1.copy(); # copies user1 to user2
print(user1.clear())
print(user2) # returns user2 since it's not cleared


#------------  Removing Items  -----------------
print(user2.pop('age')) # removes age and its value
print(user2.popitem()) # remvoes the last key-value item

user2.update({'age':30}) # updates the value, it doesn't exist, adds a new key-value
print(user2)