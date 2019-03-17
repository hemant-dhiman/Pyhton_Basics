#list a data type for mutable ordered sequences of element
#e.g.:

months = ['jan','feb','mar','apr','may','jun','july','august','sep','oct','nov','dec']
print('Normal Traverse!')
print(months[0])
print(months[1])
print(months[2])
print(months[3])
print(months[4],'\n')

#or
print('for loop Traverse!')
for  x in range(0,12):
    print(months[x])

#or
print('\nTraverse from last or with negative index!')
print(months[-1])
print(months[-2])
print(months[-3])
print(months[-4])

#list can containes different data types!
print('\nDifferent data types in list:')
list_1=['abc as string',1,2,3,"string",True,False]
for x in range(0,7):
    print(list_1[x])

#Slice And Dice Method!
print('\nSlice And Dice Method:(Also Work With String:')
months = ['jan','feb','mar','apr','may','jun','july','august','sep','oct','nov','dec']
month_2 = months[0:5]
print('Using "months[0:5]" : ',month_2)
#or
month_2 = months[:7]
print('Using "months[:7]"  : ',month_2)
#or
month_2 = months[6:]
print('Using "months[6:]"  : ',month_2)

#Membership operator in list
print('\nlist Support in or Membership operator:')
greeting_string = 'Hello There'
nice_day=['sunday','monday','tuesday','wednesday','thursday']
print('Also works in string and for list:')
print('print("hel" in greeting_string,"hel" not in greeting_string)\nprint("sunday" in nice_day,"sunday" not in nice_day)')
print('hel' in greeting_string,'hel' not in greeting_string)
print('sunday' in nice_day,'sunday' not in nice_day)

#list can be modified!
print('\nList modification!')
nice_day=['sunday','monday','tuesday','wednesday','thursday','Saturaday','Friday']
print('Before',nice_day[5])
nice_day[5]='Friday'
nice_day[6]='Saturday'
print('After',nice_day[5])
#for x in range(0,7):
#    print(nice_day[x])

#for e.g:
print('\nList modification  and string modification')
print('String:-')
name = 'jim'
student = 'name'
name = 'tim'
print(name)
print(student)
print('List:-')
score = ['A','B','B','D','A','O','B']
grade = score
print('Before:-')
print('score: ',score)
print('grade: ',grade)
score[2] = 'A'
print('After:-')
print('score: ',score)
print('grade: ',grade)

"""
Function or method for list:
"""
#len()
print(len(score))#return integer
#max()
score = ['5','2','6','3']
print(max(score))
#min()
print(min(score))
#sorted()
print('Before  sorted:',score)
print(sorted(score))
print('For reverse sort order:')
print(sorted(score,reverse=True))
#join()
List = ['A','B','C','D','E','F','G','H']
new_list = '\n'.join(List)
print(new_list)
print('\n or')
new_list = '-'.join(List)
print(new_list)
#append()//add the element to the end of the list
List = ['A','B','C','D','E','F','G','H']
print('Before: ',List)
List.append('I')
print('After: ',List)