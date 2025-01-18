#Task 5: BMI Category
 

def BMI_calculator(weight,height):
     
     
    bmi = weight/(height**2)
    
    print(f"BMI : {bmi:.2f}",end=", Category: ")
    
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5<=bmi<24.9:
        print("Normal Weight")
    elif 25 <= bmi < 29.9:
        print("Over Weight")
    elif bmi>=30:
        print("Obesity")
    else:
        print("Something wrong!")

BMI_calculator(float(input("Enter weight in kg:")), float(input("Enter height in meter:")))
        
    
    
