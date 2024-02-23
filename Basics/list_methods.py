basket = ['a','b','c','d','e']


# Adding
basket.append(100) # adds an item to the last

basket.insert(4,'hello') #adds at index 4

basket.extend([5,10]) # adds on a new list to the original
print(basket)

#Removing
basket.pop() # removes the last item; return the moved item

basket.pop(3) #removes item at index 3

basket.remove('hello') # removes 'hello'
#basket.clear() # remvoes everything from the list
print(basket)

###########
print(basket.index('e')) # returns index of 'e'
print(basket.index('c',0,4)) # looks for 'c' from index 0 to 4

print('c' in basket) # return boolean if 'c' is in basket

print(basket.count('c')) # returns # of times 'd' occurs in basket

## SORTING 
new_basket = ['a', 'x', 'e', 'i', 'b', 'o']
#new_basket.sort() #sorts the list; returns None

print(sorted(new_basket)) #returns a sorted list; doesn't change original list
new_basket.reverse() #reverses the list
print(new_basket)

### COMMON PATTERNS ------------------
print(new_basket[::-1]) # reverses the string

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'John'])
# joins each of the iterables with prior string ' ' 
print(new_sentence)  