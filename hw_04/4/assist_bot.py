def parse_input(user_input):
    """Parse user input into command and arguments."""
    parts = user_input.split()
    cmd = parts[0].strip().lower() if parts else ""
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    """Add a contact to the contacts dictionary."""
    if len(args) != 2:
        return "Invalid input. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Change an existing contact's phone number."""
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    """Show the phone number of a contact."""
    if len(args) != 1:
        return "Invalid input. Usage: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    """Show all contacts."""
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
