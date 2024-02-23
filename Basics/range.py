'''
Range 

-> a datatype to create a iterable
-> useful in looping through a certian number of times 
'''

for _ in range(0,10,2):
    print(_ + 1)

# " _ " is used when you don't care about the name of the variable and 
# just want to quickly loop over a range 

#Can also create a list with range
for _ in range(3):
    print(list(range(10)))

#Creates 3 lists of numbers from 0-9
