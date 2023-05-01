def list_drink(): 
    drink = 'randomstring'
    drinks = []
    count = 0
    while drink != '': 
        drink = input('What drink would you like to have?').lower()
        if drink != '':
            drinks += [drink]  
            count = len(drinks)
        else:
            return (drinks, count)
print(list_drink())
