def show_menu():
    print("\n📒 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

contacts = {}

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print(f"✅ {name} added successfully!")

    elif choice == "2":
        if contacts:
            print("\nYour Contacts:")
            for name, phone in contacts.items():
                print(f"{name} → {phone}")
        else:
            print("No contacts found.")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"🔍 {search} → {contacts[search]}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print(f"🗑️ {delete} deleted.")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        print("👋 Exiting Contact Book. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please try again.")
