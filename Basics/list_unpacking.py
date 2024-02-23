#List Unpacking

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
#assigns each element to the variables on left side
# 'other' contains the remaining elements in a list
print(a)
print(b)
print(c)
print(other) # prints out list of [4,5,6,7,8]
print(d)