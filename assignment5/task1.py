#Task 1: Student Performance Analysis
students = []

for i in range(10):
    print(f"Enter grades for student {i+1} (4 subjects):")
    grades = list(map(float, input().split()))
    students.append(grades)

subject_averages = [sum(subject) / 10 for subject in zip(*students)]
student_averages = [sum(grades) / 4 for grades in students]

print("\nSubject Averages:")
for i, avg in enumerate(subject_averages, 1):
    print(f"Subject {i}: {avg:.2f}")

print("\nStudent Averages:")
for i, avg in enumerate(student_averages, 1):
    print(f"Student {i}: {avg:.2f}")

print("\nHighest and Lowest Grades:")
for i, grades in enumerate(zip(*students), 1):
    print(f"Subject {i}: Highest = {max(grades)}, Lowest = {min(grades)}")

for i, grades in enumerate(students, 1):
    print(f"Student {i}: Highest = {max(grades)}, Lowest = {min(grades)}")
