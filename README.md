💸 Expense Tracker CLI
A lightweight, Python-based Command Line Interface (CLI) tool designed to help you track daily spending, monitor monthly budgets, and visualize where your money is going with data-driven charts.
🚀 Features
•	Log Expenses: Quickly add expenses with a date, category, and amount.
•	Persistent Storage: Data is saved locally in a expenses.csv file, so your records stay safe between sessions.
•	Monthly Insights: Filter and sum up total spending for a specific month.
•	Data Visualization: Generates a bar chart using Matplotlib to show spending distribution across categories.
•	Budget Guard: Set a monthly budget and instantly see if you've overspent or if you're still "in the green."
🛠️ Installation & Setup
1. Prerequisites
Ensure you have Python 3.x installed on your system. You will also need the matplotlib library for the charting feature.
2. Install Dependencies
Open your terminal or command prompt and run:
Bash
pip install matplotlib
3. Save the Script
Save the provided code into a file named expense_tracker.py.

📖 How to Use
1.	Run the application:
Bash
python expense_tracker.py
2.	Navigate the Menu:
•	Option 1: Add a new expense. If you leave the date blank, it defaults to today.
•	Option 2: View a raw list of all recorded expenses.
•	Option 3: Enter a month (e.g., 2024-05) to see total spending for that period.
•	Option 4: View a summary of spending by category and trigger a pop-up bar chart.
•	Option 5: Input a budget limit to check your current month's financial health.
•	Option 6: Safely exit the program.
📂 File Structure
•	expense_tracker.py: The main Python script.
•	expenses.csv: Created automatically on the first run; stores all your transaction data.

