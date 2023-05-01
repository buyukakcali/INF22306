import shelve


def check_person(phonebook, name):
    return name in phonebook

def lookup(phonebook, name):
    print("I am looking up the number of you")
    if check_person(phonebook, name):
        number = phonebook.get(name)
    else:
        number = "dummy"
    return number

def enter(phonebook, name, number):
    print("I am going to enter this for you")
    phonebook[name] = number
# new_contact = {
#     name : number
# }
# phonebook.update(new_contact)

def remove(phonebook, name):
    phonebook.pop(the_name)
    print("I am deleting this person from your phonebook")

def help_app():
    print("You can do lookup / enter / remove; type quit to stop")

def quit_app():
    print("Thank you, goodbye!")


# main program
with shelve.open("f3_6_phonebook_data.shelve") as the_phonebook:
    print("Welcome to the phonebook program")
    help_app()
    user_input = "dumy"
    while user_input != "quit":
        user_input = input("What would you like to do: ")

        if user_input == "lookup":
            the_name = input("Which name do you want to lookup? ")
            if check_person(the_phonebook, the_name):
                the_number = lookup(the_phonebook, the_name)
                print(f"The number for {the_name} is ", the_number)
            else:
                print(f'The person you have look up \"{the_name}\" hasn\'t got a number in the phonebook')

        elif user_input == "enter":
            the_name = input("Which name do you want to enter? ")
            the_number = input("What number does this person have? ")
            if not check_person(the_phonebook, the_name):
                enter(the_phonebook, the_name, the_number)
            else:
                print("The person, you want to add is already in phonebook!")

        elif user_input == "remove":
            the_name = input("Which name do ou want to remove? ")
            if check_person(the_phonebook, the_name):
                remove(the_phonebook, the_name)
            else:
                print(f'The person you want to delete is already not in the phonebook!')
        elif user_input == "quit":
            quit_app()
        else:
            help_app()
    the_phonebook.close()
