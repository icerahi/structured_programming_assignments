#5. Personal Diary Application

diary = {}

def add_entry(date, content):
    if date in diary:
        diary[date].append(content)
    else:
        diary[date] = [content]

def view_entries():
    for date, entries in diary.items():
        print(f"{date}:")
        for entry in entries:
            print(f"- {entry}")

def delete_entry(date):
    if date in diary:
        del diary[date]
    else:
        print("No entries found for the given date.")

while True:
    print("\n1. Add Entry\n2. View Entries\n3. Delete Entry\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        content = input("Enter content: ")
        add_entry(date, content)
    elif choice == "2":
        view_entries()
    elif choice == "3":
        date = input("Enter date to delete (YYYY-MM-DD): ")
        delete_entry(date)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
