import handler

def main():
    print("Welcome to the Phone Bot!")
    contacts = {}

    while True:
        user_input = input("Please enter a command: ")
        try: 
            cmd, *args = handler.parse_input(user_input)

            # Command handling
            if cmd in ["exit", "close"]:
                print("Good bye!")
                break
            # hello command actions
            elif cmd == "hello":
                print("Hello! Can i help you")
            
            # add command actions
            elif cmd == "add":
                if len(args) < 2:
                    print("Usage: add <name> <phone>")
                else:
                    if handler.add_contact(args, contacts):
                        print("Contact added.")
                    else:
                        print("Invalid phone number format. Please use a valid format (9-12 digits).")
            
            # change command actions                
            elif cmd == "change":
                if len(args) < 2:
                    print("Usage: change <name> <phone>")
                else:
                    if args[0] not in contacts:
                        print("Contact not found.")
                        continue
                    if handler.change_contact(args, contacts):
                        print("Phone number changed.")
                    else:
                        print("Invalid phone number format. Please use a valid format (9-12 digits).")

            # phone command actions
            elif cmd == "phone":
                if len(args) < 1:
                    print("Usage: phone <name>")
                else:
                    print(handler.show_phone_number(args, contacts))
            
            # all command actions
            elif cmd == "all":
                print(handler.show_all_contacts(contacts))
            elif cmd == "help":
                print("\nAvailable commands: add, change, phone, all, exit, close\
                    \nadd <name> <phone> - add a new contact\
                    \nchange <name> <phone> - change an existing contact\
                    \nphone <name> - show a contact's phone number\
                    \nall - show all contacts\
                    \nclose, exit - close the application\
                    \n<phone> must have 9-12 digits and can started with +")
            else:
                print("Unknown command")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
