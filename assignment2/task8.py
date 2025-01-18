#Task 8: Grade Calculator

def grade_calculator():
    homework=float(input("Enter homework score (0-100):"))
    midterm=float(input("Enter midterm score (0-100):"))
    final_exam=float(input("Enter final exam score (0-100):"))
    
    if (0 <= homework <= 100) and (0 <= midterm <= 100) and (0 <= final_exam <= 100):
        final_grade=(homework*0.40)+(midterm*0.30)+(final_exam*0.30)
        print(f"Your Final Grade is: {final_grade:.2f}")
        if final_grade>=60:
            print("Congrats! You passed.")
        else:
            print("Sorry! You failed")
    else:
        print("Invalid Input")
grade_calculator()