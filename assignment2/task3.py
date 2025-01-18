#Task 3: Age Group Classification

def age_group(age):
    if(age>0 and age<12):
        print("Child")
    elif(age>13 and age<19):
        print("Teenager")
    elif(age>20 and age<64):
        print("Adult")
    elif(age>65):
        print("Senior")
    else:
        print("Invalid Input")
        
age_group(int(input("Enter Age:")))