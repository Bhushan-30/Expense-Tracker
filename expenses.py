import csv
import calendar
import datetime
from ex import expense

def main():
    # Ask for the monthly budget and ensure valid input.
    while True:
        try:
            budget = float(input('Enter the Budget: Rs. '))
            break
        except ValueError:
            print("Invalid input! Budget must be a numeric value.")

    # Allow the user to enter multiple expenses.
    expenses = []
    while True:
        add = input("\nWould you like to add a new expense? (y/n): ").lower().strip()
        if add == 'y':
            new_exp = check_expense()
            expenses.append(new_exp)
        elif add == 'n':
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

    expense_file_path = 'expense.csv'
    
    # Save the list of expenses to the CSV file.
    save_expenses(expenses, expense_file_path)
    
    # Display the summary of expenses.
    summerise_expense(expense_file_path, budget)

def check_expense():
    print("\nEnter the expense details:")
    expense_name = input('Expense name: ')
    
    # Safely capture the expense amount.
    while True:
        try:
            expense_amount = float(input('Expense amount (Rs.): '))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    expense_categories = ['Food', 'Travel', 'Entertainment', 'Accommodation', 'Shopping', 'Others']
    
    # Loop until a valid category is selected.
    while True:
        print("\nSelect a category:")
        for i, cat in enumerate(expense_categories, start=1):
            print(f'{i}. {cat}')
        try:
            select_index = int(input(f'Select category number [1-{len(expense_categories)}]: ')) - 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        if 0 <= select_index < len(expense_categories):
            selected_category = expense_categories[select_index]
            print(f'You selected: {selected_category}')
            return expense(expense_name, expense_amount, selected_category)
        else:
            print("Invalid category choice. Please try again.")

def save_expenses(expense_list, expense_file_path):
    print(f"\nSaving expenses to {expense_file_path} ...")
    # Append mode with newline='' to prevent extra blank lines on some platforms.
    with open(expense_file_path, 'a', newline='') as csvfile:
        expense_writer = csv.writer(csvfile)
        for exp in expense_list:
            # Write each expense to the CSV
            expense_writer.writerow([exp.name, f'{exp.amount:.2f}', exp.category])
    print("Expenses saved successfully!")

def summerise_expense(expense_file_path, budget):
    print("\n--- Expense Summary ---")
    expenses = []
    # Read the CSV file and reconstruct expense objects.
    with open(expense_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        expense_reader = csv.reader(csvfile)
        for row in expense_reader:
            if not row:
                continue  # Skip blank lines if any.
            try:
                name, amount, category = row
                exp_obj = expense(name, float(amount), category)
                expenses.append(exp_obj)
            except ValueError:
                print("Error processing row:", row)
                continue

    if not expenses:
        print("No expenses recorded.")
        return

    # Calculate total expense by category.
    amount_by_category = {}
    for exp in expenses:
        amount_by_category[exp.category] = amount_by_category.get(exp.category, 0) + exp.amount

    for cat, amt in amount_by_category.items():
        print(f'{cat}: Rs.{amt:.2f}')
    
    total_expense = sum(exp.amount for exp in expenses)
    print(f'\nTotal Expense: Rs.{total_expense:.2f}')
    
    remaining_amount = budget - total_expense
    print(f'Remaining Budget: Rs.{remaining_amount:.2f}')

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    if remaining_days > 0:
        daily_budget = remaining_amount / remaining_days
        print(f'Daily Available Budget for the rest of the month: Rs.{daily_budget:.2f}')
    else:
        print("No remaining days in the month!")

if __name__ == "__main__":
    main()
