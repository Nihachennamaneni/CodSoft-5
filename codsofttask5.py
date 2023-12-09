class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact.name} - {contact.phone}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_key):
        found = False
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone:
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                contact.name = new_contact.name
                contact.phone = new_contact.phone
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, delete_name):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == delete_name.lower():
                del self.contacts[idx]
                print("Contact deleted.")
                return
        print("Contact not found.")

def main():
    my_contacts = ContactBook()

    while True:
        print("\nWelcome to the Contact Book!")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            my_contacts.add_contact(contact)

        elif choice == '2':
            my_contacts.view_contacts()

        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            my_contacts.search_contact(search_key)

        elif choice == '4':
            old_name = input("Enter name of contact to update: ")
            new_name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(new_name, phone, email, address)
            my_contacts.update_contact(old_name, new_contact)

        elif choice == '5':
            delete_name = input("Enter name of contact to delete: ")
            my_contacts.delete_contact(delete_name)

        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
