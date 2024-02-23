'''
Sets
--> Unordered collection of unique items; can be used to remove 
    duplicates from Lists
--> doesn't support indexing
'''

my_set = {1,2,3,4,5,5}
print(my_set); #prints only one 5

print(len(my_set))
print(5 in my_set)

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(list(new_set))

your_set = {4,5,6,7,8,9,10}

print(new_set.difference(your_set)) #prints elements not in your_set
new_set.discard(5) # removes 5 from the set
print(new_set)

new_set.difference_update(your_set) #updates new_set with just the difference
print(new_set)
print(new_set.intersection(your_set)) # prints just the common elements

print(new_set.isdisjoint(your_set)) # if they don't have any common elements returns True

other_set = {4,5,6}

print(other_set.issubset(your_set)) # checks if one is subset of the other
print(your_set.issuperset(other_set)) #checks if your_set entirely contains other_set
print(new_set.union(your_set)) #combines 2 sets, removing any duplicates
