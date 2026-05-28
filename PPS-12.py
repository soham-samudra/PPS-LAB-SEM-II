# Initialize empty phonebook
phonebook = {}

# Read number of operations
n = int(input())

for _ in range(n):
    command = input().strip().split()

    if command[0] == "ADD":
        name = command[1]
        phone_number = command[2]
        # Add or update contact
        phonebook[name] = phone_number

    elif command[0] == "REMOVE":
        name = command[1]
        # Remove contact if exists
        if name in phonebook:
            del phonebook[name]

    elif command[0] == "DISPLAY":
        if not phonebook:
            print("No contacts")
        else:
            # Print contacts sorted by name
            for name in sorted(phonebook.keys()):
                print(f"{name}: {phonebook[name]}")
