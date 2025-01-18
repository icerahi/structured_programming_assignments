#2. Expense Tracker

all_data=[]

def add_expenses():
    amount=int(input("add expense amount:"))
    expense_type=input("Expense Type: ")
    all_data.append({"amount":amount,"expense_type":expense_type})
    print("Added Successfully")
    
def total_expenditure():
    total=0
    for data in all_data:
        total+=data["amount"]
        
    print(f"***Total Expenditure: {total} ***")
    print()

def view_expense_details():
    total_expenditure()
    print("Expense Type | Amount")
    for data in all_data:
        expense_type=data["expense_type"]
        amount=data["amount"]
        print(f"{expense_type:5} | {amount:5}")

def main():
    while True:
        print("**Expense Tracker**")
        print("""
          1.Add Expense
          2.View Expenses
          0.Exit""")
        option=int(input("Choose option:"))
        if option==1:
            add_expenses()
        elif option==2:
            view_expense_details()
        elif option==0:
            break
        else:
            print("invalid input!")
main()