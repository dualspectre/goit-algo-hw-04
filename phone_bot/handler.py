import re

pattern = r"^[+]?\d{9,12}$"
#function of parsing user input command
def parse_input(user_input): 
    """
    Parses the user input command and returns the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#function of adding a contact
def add_contact(args, contacts):
    """
    Adds a new contact to the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts
    """
    if len(args) < 2:
        print("Usage: add <name> <phone>")
    else:
        name, phone = args
        condition = bool(re.fullmatch(pattern, phone))
        if condition:
            contacts[name] = phone
            print("Contact added.")
        else:
            print("Invalid phone number format. Please use a valid format (9-12 digits).")

#function of changing a contact
def change_contact(args, contacts):
    """
    Changes an existing contact in the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts
    """
    if len(args) < 2:
        print("Usage: change <name> <phone>")
    else:
        name, phone = args
        if name not in contacts:
            print("Contact not found.")
            return
        condition = bool(re.fullmatch(pattern, phone))
        if condition:
            contacts[name] = phone
            print("Phone number changed.")
        else:
            print("Invalid phone number format. Please use a valid format (9-12 digits).")

#function of showing a contact's phone number
def show_phone_number(args, contacts):
    """
    Shows a contact's phone number.
    Input: args - list of arguments, contacts - dictionary of contacts
    """
    if len(args) < 1:
        print("Usage: phone <name>")
    else:
        name = args[0]
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")

#function of showing all contacts
def show_all_contacts(contacts):
    """
    Shows all contacts in the contacts dictionary.
    Input: contacts - dictionary of contacts
    """
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")