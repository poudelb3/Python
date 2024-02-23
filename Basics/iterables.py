# Iterables
# a collection of items that can be iterated over, meaning
# each item can be check one-by-one
# e.g string, list, set, tuple, dictionary

user = dict(name = 'Golem', 
            age = 30, 
            can_swim = False)

# Dictionary can be iterted in 3 ways: 
# Geting items
for items in user.items():
    print(items) # prints key-value pairs
#--------------------------------------------------------------------------
#can also print keys and values separately, instead of a tuple like above
for key, value in user.items():
    print(key, value)
#--------------------------------------------------------------------------

# Getting just the values
for items in user.values():
    print(items)

#Getting just the keys
for items in user.keys():
    print(items)

## iterting over just the variable name gives keys
for items in user:
    print(items)

