#Logical Operator = and,or,not
#bitwise and symbol &
#bitwise or symbol |
#bitwise not symbol ~
print('e.g for and operator X=True and Y=false')
x = True
y= False
print('X & X = ',x and x)
print('X & y = ',x and y)
print('y & X = ',y and x)
print('y & y = ',y and y)

print('e.g for or operator X=True and Y=false')
print('X | X = ',x or x)
print('X | y = ',x or y)
print('y | X = ',y or x)
print('y | y = ',y or y)

print('e.g for not operator X=True and Y=false')
print('~ X = ',not x)
print('~ y = ',not y)
print('~ x & y',not(x and y))

#bitwise  e.g.
print('Bitwise and , or , not!')
print('bitwise and(x & y) =',x & y)
print('bitwise or(x | y) =',x | y)
print('bitwise not y(~ y) =',~ y)
print('bitwise not x(~ x) =',~ x)