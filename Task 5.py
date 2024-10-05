# Function to add a new contact
def add_contacts(num):
    for _ in range(num):
        name = input("Enter contact name: ").strip().title()
        while True:
            contact_number = input("Enter contact number (digits only): ")
            if contact_number.isdigit() and len(contact_number) >= 7:
                contact_number = int(contact_number)
                break  # Valid number, break the loop
            else:
                print("Please enter a valid phone number with digits only and at least 7 digits.")
        
        contacts[name] = contact_number  # Store name and number in the dictionary

# Function to display all contacts
def display_contacts():
    if contacts:
        print("\nName\t\t\tContact Number\n" + "-"*40)
        for name, contact_number in contacts.items():
            print(f"{name:<20} {contact_number}")
    else:
        print("\nNo contacts saved yet.")

# Function to search for a contact by name
def search_contact():
    search_term = input("\nEnter search term: ").strip().title()
    print("\nSearch results:")

    found = False
    for name, number in contacts.items():
        if search_term in name:
            print(f"Name: {name}, Phone Number: {number}")
            found = True

    if not found:
        print("No matching contact found.")

# Main logic for the contact management system
if __name__ == "__main__":
    contacts = {}  # Dictionary to store contacts as name: number pairs

    num = int(input("Enter the total number of contacts you want to save: "))
    add_contacts(num)

    # Display all contacts
    display_contacts()

    while True:
        # Prompt for searching contacts
        search_choice = input("\nDo you want to search for a contact? (y/n): ").lower()
        if search_choice == 'y':
            search_contact()
        elif search_choice == 'n':
            print("\nThanks for using the contact manager!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
