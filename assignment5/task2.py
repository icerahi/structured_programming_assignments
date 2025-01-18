#Task 2: Seating Arrangement

seating = [[0 for _ in range(10)] for _ in range(10)]
def display_seating():
    print("***Display Seating****")
    for row in seating:
        print(row)

def reserve_seat(row, col):
    print(seating[row][col])
    if seating[row][col] == 0:
        seating[row][col] = 1
        print("Seat reserved.")
    else:
        print("Seat already reserved.")

def cancel_seat(row, col):
    if seating[row][col] == 1:
        seating[row][col] = 0
        print("Reservation canceled.")
    else:
        print("Seat is not reserved.")
        
while True:
    print("\n1. Display Seating\n2. Reserve Seat\n3. Cancel Seat\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        display_seating()
    elif choice == "2":
        row = int(input("Enter row (0-9): "))
        col = int(input("Enter column (0-9): "))
        reserve_seat(row, col)
    elif choice == "3":
        row = int(input("Enter row (0-9): "))
        col = int(input("Enter column (0-9): "))
        cancel_seat(row, col)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")






