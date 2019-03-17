'''
syntax
dics = {key: values,key: values.....}

Each item in a dictionary contains two parts (a key and a value), the items in a dictionary are not ordered,
and we can see examples of nested dictionaries in next file 9.1.
Because dictionaries are not ordered, they are not sortable. And you do not add items to a dictionary with .append.
'''

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
from builtins import print

population = {'Shanghai': 17.8,'Istanbul': 13.3,'Karachi': 13.0,'Mumbai': 12.5,}
print(population,' and type is: ',type(population))
#Which of these could be used as the key for a dictionary
population = {'Shanghai': 17.9,13.5: 13.3,1: 13.0}
print(population,' and type is: ',type(population))

print(population['Shanghai'])#key can be string
print(population[13.5])#key can be of type float
print(population[1])#key can be of type int
#print(population[1,1,6])#key can't be of type list
#print(population['ram'])
print(population.get('dilithium'))
print(population.get('Shanghai'))
print(population.get('kryptonite', 'There\'s no such element!'))
#Checking for Equality vs. Identity: == vs. is
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)


population = {'Shanghai': [2,4,3,6,23],'Istanbul': 13.3,'Karachi': 'str','Mumbai': 12.5,}
print(population['Shanghai'][4])
#Compound Data Structures