# *args & **kwargs
'''
*args
-> allows to pass any number of arguments in a function
-> can use any names, 'args' is just a standard in Python Community
    for e.g *value, *sth, are also valid
-> passed arguments stored as a tuple

**kwargs
-> allows to pass any number of KEYWORD ARGUMENTS in a function
-> passed arguments stored in a dictionary
'''

def super_fun(*args, **kwargs):
    total = 0
    print(kwargs)
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_fun(1,2,3,4,5, num1 = 5, num2 = 10))

'''
If there are other arguments in the functions, the order is this: 
parameters, *args, default parameters, **kwargs

'''