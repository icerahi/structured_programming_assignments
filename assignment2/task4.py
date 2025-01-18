#Task 4: Menu-Driven Calculator

menu="""
1.Addition
2.Subtraction
3.Multiplication
4.Division
"""

def calculator(number1,number2):
    print(menu)
    option=int(input("Choose an option:"))
    
    if(option==1):
        print(number1+number2)
    elif(option==2):
        print(number1-number2)
    elif(option==3):
        print(number1*number2)
    elif(option==4):
        try:
            print(number1/number2)
        except ZeroDivisionError as e:
            print(e)
    else:
        print("Invalid Input")
        
calculator(int(input("Enter number 1:")),int(input("Enter number 2:")))