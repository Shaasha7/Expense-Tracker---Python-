# Expense-Tracker---Python-
A simple yet powerful Expense Tracker built using Python and Object-Oriented Programming (OOP). This project helps users manage daily expenses by adding, viewing, and categorizing them efficiently.
# 💰 Expense Tracker - Python Project

A simple **Expense Tracker application** built using Python and Object-Oriented Programming (OOP). This project helps users manage their daily expenses efficiently by adding, viewing, and categorizing them.

---

## 🚀 Features

* Add new expenses with category, amount, and note
* View all recorded expenses
* Calculate total spending
* Category-wise expense summary

---

## 🛠 Tech Stack

* Python 🐍
* Object-Oriented Programming (OOP)
* Command Line Interface (CLI)

---

## 📌 How to Run

1. Clone the repository
2. Open terminal in project folder
3. Run the file:

```bash
python expense_tracker.py
```

---

## 💻 Code

```python
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
```
<img width="1812" height="932" alt="1" src="https://github.com/user-attachments/assets/fa99885b-75cb-4f28-b217-eb8fc4176ebf" />
<img width="1887" height="688" alt="1" src="https://github.com/user-attachments/assets/a2bb5e6a-215a-47a4-aa1b-19f3a2da59c0" />
<img width="1697" height="883" alt="2" src="https://github.com/user-attachments/assets/cdca1429-a190-4282-b0cf-dc87cfcc65ab" />

---

## 🎯 Learning Outcomes

* Object-Oriented Programming (OOP)
* Data structures (lists & dictionaries)
* Real-world problem solving
* CLI-based application development

---

## 📸 Future Improvements

* GUI using Tkinter or Streamlit
* Database integration (SQLite)
* Graph-based analytics

---

## 👨‍💻 Author

Built with ❤️ using Python for learning and portfolio purposes.
