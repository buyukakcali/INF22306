def list_drink():
    drink = 'randomstring'
    drinks = []
    count = 0
    while drink != '':
        drink = input('What drink would you like to have?').lower()
        if drink != '':
            drinks += [drink]  # This is my only mistake (converting the drink variable to an element of a list) after
            # the exam notes..
            count = len(drinks)
        else:
            return (drinks, count)


print(list_drink())
