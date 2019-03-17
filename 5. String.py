"""
Strings
includes Letters,Numbers,Spaces & Symbols
print using print() function!
"""

print('Hello World!!') #created using '
print("Hello World!!") #created using "

"""
Operation for String
+ -> To combine Strings
* -> To Repeat String

"""
print('\nFirst Operator "+"')
f_word='Hello'
l_word='World!!'
print(f_word+l_word)

print('\nSecond Operator "*"')
string='Love'
print(string*5)

"""
Built-in Function for String
len()-> it returns the length of string variable as integer (e.g: len(var))
lower()->it use to conver all letter of string to lowercase (e.g:var.lower())
title()->it use to capitalize each first letter of words in string!(var.title())
count()->it use to count the repeated word in a string and return integer.
(var.count(string_which_u_want_to_find))

foramat() -> it is use to give the value to placeholder!
"""
print('\nlength() function')
String_length=len(f_word+l_word)
print(f_word+l_word)
print('Length of String_Length',String_length)

print('\nlower() function')
Cap_string='CAPITAL STRING'
print('Before func. apply:',Cap_string,'\nAfter apply func: ',Cap_string.lower())
#or
print('CAPITAL STRING'.lower())

print('\ntitle() function')
lower_string='it is a string having all char lowercase!'
print('Before func. apply:',lower_string,'\nAfter apply func: ',lower_string.title())
print('it is a string having all char lowercase!'.title())

print('\ncount() function')
count_string='one fish,two fish,three fish,four fish'
print('How many times "fish" repeats in this string: ',count_string,'=',count_string.count("fish"),'times')

print('\nformat() function')
print('Hemant has {} ball'.format(100))
animal = 'Dog'
action = 'Bite'
print('Does your {} {}?'.format(animal,action))

print('\nSlice and dice method in String: Fro e.g:')
print("greeting_string = 'Hello There'\nprint(greeting_string[6:9])\nprint('O/p: ',greeting_string[2:5])")
greeting_string = 'Hello There'
print('O/p: ',greeting_string[6:9])
print('O/p: ',greeting_string[2:5])

'''
there are several methods for string data  type:
capitalize()
encode()
format()
isalpha()
islower()
istitle()
casefold()
endwith()
format_map()
isdecimal()
isnumeric()
isupper()
center()
expandtabs()
index()
isdigit()
isprintable()
join()
count()
find()
isalnum()
isidentifier()
isspace()
'''