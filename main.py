contacts = {}  # Словник для збереження контактів

def add_contact(name, phone):
    if name in contacts:
        return f"Contact {name} already exists."
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."

def change_contact(name, phone):
    if name not in contacts:
        return f"Contact {name} not found."
    contacts[name] = phone
    return f"Contact {name} updated with new phone {phone}."

def get_phone(name):
    if name not in contacts:
        return f"Contact {name} not found."
    return f"The phone number for {name} is {contacts[name]}."

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
    return wrapper

@input_error
def handle_command(command, *args):
    if command == "add":
        return add_contact(*args)
    elif command == "change":
        return change_contact(*args)
    elif command == "phone":
        return get_phone(*args)
    elif command == "show all":
        return show_all_contacts()
    elif command in ["good bye", "close", "exit"]:
        return "Good bye!"
    elif command == "hello":
        return "How can I help you?"
    else:
        return "Unknown command"

def parser(text):
    parts = text.split(" ", 1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    return command, args

def main():
    while True:
        user_input = input(">>>")
        if user_input.lower() in ["good bye", "close", "exit"]:
            print(handle_command(user_input))
            break
        command, args = parser(user_input)
        result = handle_command(command, *args.split())
        print(result)

if __name__ == "__main__":
    main()
