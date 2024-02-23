'''
Enumerate: 

-> iterates over, but also gives index of each item 
-> llike Range function, but keeps track of index as well
'''

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i,char)