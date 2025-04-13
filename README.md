# 📈 Expense Tracker CLI

A simple and efficient **command-line application** built with Python to help you **track your monthly expenses**, **manage your budget**, and **analyze your spending habits**.

## 🛠️ Project Overview

This project allows users to:

- Set a **monthly budget**.
- **Add and categorize** multiple expenses.
- **Save** expenses to a CSV file (`expense.csv`).
- **Summarize** expenses by category and show:
  - Total spent
  - Remaining budget
  - Daily available budget for the rest of the month

Designed to be minimal, fast, and run completely in the terminal with no external dependencies.

## 📂 Files and Structure

- **`ex.py`** — Defines the `expense` class to represent individual expense entries.
- **`expenses.py`** — Main application logic for interacting with the user, recording expenses, and generating summaries.
- **`expense.csv`** — Data file where all expenses are saved for persistence between sessions.

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine.

No additional libraries are required beyond the Python standard library (`csv`, `datetime`, `calendar`).

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Run the program**:

```bash
python expenses.py
```

3. **Follow the on-screen instructions** to add expenses and view your spending summary.

## 🧹 Features

- **Simple Interface**: Text-based prompts for easy interaction.
- **Dynamic Category Selection**: Choose categories like Food, Travel, Entertainment, Shopping, etc.
- **Data Persistence**: Expenses are saved to `expense.csv` automatically.
- **Budget Tracking**: Real-time tracking of total spent, remaining budget, and daily allowance.
- **Error Handling**: Graceful handling of invalid inputs.

## 📸 Example Usage

```
Enter the Budget: Rs. 50000

Would you like to add a new expense? (y/n): y
Expense name: Lunch
Expense amount (Rs.): 250
Select a category:
1. Food
2. Travel
3. Entertainment
4. Accommodation
5. Shopping
6. Others
Select category number [1-6]: 1
You selected: Food

Would you like to add a new expense? (y/n): n

--- Expense Summary ---
Food: Rs.250.00

Total Expense: Rs.250.00
Remaining Budget: Rs.49750.00
Daily Available Budget for the rest of the month: Rs.1658.33
```

## 📌 Notes

- Every time you run the program, **new expenses are appended** to `expense.csv`.
- To **reset your data**, manually delete or clear the `expense.csv` file.

## ✨ Future Improvements

- Option to edit or delete an expense.
- Monthly graphs and visualizations using `matplotlib`.
- Separate expense files for each month.
- Command-line arguments for faster operation (e.g., `--add`, `--summary`).

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements.

---

## 🧠 Author
👤 Bhushan Deshmukh
📨 bsdeshmukh98@gmail.com

