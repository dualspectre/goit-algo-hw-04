import handler

def main():
    print("Welcome to the Phone Bot!")
    contacts = {}

    while True:
        user_input = input("Please enter a command: ")
        try: 
            cmd, *args = handler.parse_input(user_input)

               
            if cmd in ["exit", "close"]:
                print("Good bye!")
                break
            elif cmd == "hello":
                print("Hello! Can i help you")
            elif cmd == "add":
                handler.add_contact(args, contacts)
            elif cmd == "change":
                handler.change_contact(args, contacts)
            elif cmd == "phone":
                handler.show_phone_number(args, contacts)
            elif cmd == "all":
                handler.show_all_contacts(contacts)
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
