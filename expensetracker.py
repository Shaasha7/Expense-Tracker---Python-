class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, note):
        self.expenses.append({
            "category": category,
            "amount": amount,
            "note": note
        })
        print("Expense added successfully!")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\n--- Expense List ---")
        total = 0
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. {exp['category']} - ₹{exp['amount']} ({exp['note']})")
            total += exp['amount']

        print(f"\nTotal Expense: ₹{total}")

    def category_summary(self):
        summary = {}
        for exp in self.expenses:
            cat = exp["category"]
            summary[cat] = summary.get(cat, 0) + exp["amount"]

        print("\n--- Category-wise Summary ---")
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")


# ---------- Main Program ----------
tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cat = input("Enter category: ")
        amt = float(input("Enter amount: "))
        note = input("Enter note: ")
        tracker.add_expense(cat, amt, note)

    elif choice == "2":
        tracker.show_expenses()

    elif choice == "3":
        tracker.category_summary()

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice!")
