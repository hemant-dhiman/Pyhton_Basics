elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

#We can access elements in this nested dictionary like this.
helium = elements["helium"]  # get the helium dictionary
print(helium)

hydrogen_weight = elements["hydrogen"]["weight"] # get hydrogen's weight
print('Weight of hydrogen: ',hydrogen_weight)

#You can also add a new key to the element dictionary.
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)

#add nested dics
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

#todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
#hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas']= False
elements['helium']['is_noble_gas']= True
print(elements['hydrogen'])
print(elements['helium'])

#add new dictionaries into dicstionary
is_noble_gas = {'is_noble_gas': False}
elements['hydrogen']['is_noble_gas']=is_noble_gas

is_noble_gas = {'is_noble_gas': True}
elements['helium']['is_noble_gas']=is_noble_gas

print(elements['hydrogen'])
print(elements['helium'])

print('helium: ',elements['helium']['is_noble_gas'])
print('hydrogen: ',elements['hydrogen']['is_noble_gas'])