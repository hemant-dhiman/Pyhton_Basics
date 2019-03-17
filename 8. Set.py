#set
'''
Sets are not ordered, so the order in which items appear can be inconsistent and you add items to sets with .add().
Like dictionaries and lists, sets are mutable.
You cannot have the same item twice and you cannot sort sets. For these two properties a list would be more appropriate.
'''
n = [1,2,2,3,3,3,4,4,4,4]
print('Length: ',len(n),' and elements: ',n)
set_from_n = set(n)
print('Length: ',len(set_from_n),' and elements: ',set_from_n)

#define a set
set_1 = {'apple','orange','banan','mango','grapes'}
print('Length: ',len(set_1),' and elements: ',set_1)

print('watermelon' in set_1)

set_1.add('watermelon') #add a value or element
print(set_1)

#remove random element using pop() function
set_1.pop()
print(set_1)