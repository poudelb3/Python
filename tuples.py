'''
Tuplessss
--> Similar to Lists, but are IMMUTABLE
--> Can index like Lists 
'''

my_tuple = (1,2,3,4,5, 3)
print(my_tuple[3])

print(5 in my_tuple)
print(my_tuple)

# Unpacking like Lists
x,y, *other = ('a', 'b', 'c', 1, 3, 4); 
print(x); print(y), print(other)

# Just 2 METHODS 
print(my_tuple.count(3)); # returns 2
print(my_tuple.index(5)); # returns index of 5
print(len(my_tuple)); #retuns length of the tuple