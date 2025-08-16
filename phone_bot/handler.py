import re

# Regular expression pattern for validating phone numbers
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
def add_contact(args, contacts: dict) -> bool:
    """
    Adds a new contact to the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: bool - True if contact was added, False otherwise
    """
    name, phone = args
    condition = bool(re.fullmatch(pattern, phone))
    if condition:
        contacts[name] = phone
    return condition


#function of changing a contact
def change_contact(args, contacts: dict) -> bool:
    """
    Changes an existing contact in the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: bool - True if contact was changed, False otherwise
    """
    
    name, phone = args            
    condition = bool(re.fullmatch(pattern, phone))
    if condition:
        contacts[name] = phone
    return condition

#function of showing a contact's phone number
def show_phone_number(args, contacts: dict) -> str:
    """
    Shows a contact's phone number.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: str - the contact's phone number or an error message
    """
    
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

#function of showing all contacts
def show_all_contacts(contacts: dict) -> str:
    """
    Shows all contacts in the contacts dictionary.
    Input: contacts - dictionary of contacts

    Return: str - all contacts or an error message
    """
    if not contacts:
        return "No contacts found."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()