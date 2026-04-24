import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

# Initialize file

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])


# Add Expense

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added!\n")


# View Expenses

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


# Monthly Summary

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print(f"💰 Total spending in {month}: {total}\n")


# Category-wise Summary

def category_summary():
    data = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in data:
                data[category] += amount
            else:
                data[category] = amount

    print("📊 Category-wise spending:")
    for cat, amt in data.items():
        print(f"{cat}: {amt}")

    # Plot chart
    plt.bar(data.keys(), data.values())
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()


# Budget Warning

def budget_check():
    limit = float(input("Enter your monthly budget: "))
    month = datetime.today().strftime('%Y-%m')
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print(f"Current spending: {total}")

    if total > limit:
        print("⚠️ Budget exceeded!\n")
    else:
        print("✅ Within budget.\n")


# Menu

def menu():
    init_file()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary (with chart)")
        print("5. Check Budget")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            budget_check()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")


# Run program

if __name__ == "__main__":
    menu()