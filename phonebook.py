#phonebook.py

phonebook = {'Bob': '973-555-1212'}

while True:
    print("""
Welcome to the Phonebook App!
1. Add contact
2. Delete contact
3. View contacts
4. Quit
""")
    try:
        response = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    
    if response == 1:
        print("Add Contact")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        phonebook[name] = phone
        print(f"Contact '{name}' added!\n")

    elif response == 2:
        print("Delete Contact")
        name = input("Enter name to Delete: ")
        if name in phonebook:
            phonebook.pop(name)
            print(f"Contact '{name}' deleted!\n")
        else:
            print("Contact is not in Phonebook.\n")

    elif response == 3:
        if phonebook:
            print("Contacts:")
            for key, value in phonebook.items():
                print(f"Name: {key}, Phone: {value}")
            print()
        else:
            print("Phonebook is empty.\n")

    elif response == 4:
        print("Quitting Program. Goodbye!")
        break

    else:
        print("Invalid input, please try again.")