#List slicing 
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'

new_cart = amazon_cart 
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart) #prints the same as new_cart
#since both are pointing to the same address in memory

#List copying
#To copy amazon_cart use [:]
amazon_cart2 = [
    'sweatpants',
    'backpack',
    'earpods',
    'book'
]

new_cart2 = amazon_cart2[:] #copies to a new list
new_cart2 [0] = 'sunscreen'

print(new_cart2)
print(amazon_cart2)