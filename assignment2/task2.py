#Task 2: Leap Year Checker

def leap_year(year):
    if((year%4==0 and year%100!=0) or (year%400==0)):
        print("Leap Year")
    else:
        print("not leap year")
    
leap_year(int(input("Enter Year: ")))