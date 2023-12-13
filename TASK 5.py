class Contact_Book:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = [
            contact for contact in self.contacts
            if (search_term.lower() in contact.name.lower() or
                search_term in contact.phone_number)
        ]

        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("Matching Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System:")
        print("I. Add Contact")
        print("II. View Contacts")
        print("III. Search Contact")
        print("IV. Update Contact")
        print("V. Delete Contact")
        print("VI. Exit")

        choice = input("Enter your choice (I-VI): ")

        if choice == "I":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact_Book(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "II":
            contact_manager.view_contacts()

        elif choice == "III":
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)

        elif choice == "IV":
            name = input("Enter name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == "V":
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "VI":
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
