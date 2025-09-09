import json
import os

FILE_NAME = "expenses.json"

# Load existing expenses
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Add new expense
def add_expense(expenses):
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = 0
    print("\n📋 Expense List:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']}")
        total += expense['amount']
    print(f"\n💰 Total Expenses: ₹{total}\n")

# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
