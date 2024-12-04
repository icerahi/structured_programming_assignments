"""
Body Mass Index (BMI) Calculator

Write a program that calculates and outputs the Body Mass Index (BMI) given a person's weight and height. 
The BMI is calculated using the formula:

BMI=Weight (Kg)/ Height (m)^2

Allow the user to input their weight in pounds and height in inches, 
and convert these to kilograms and meters, respectively. 
Output the BMI and categorize it as underweight, normal weight, overweight, or obese.
"""

def BMI_calculator(weight,height):
    weight_in_kg= weight * 0.453592
    
    height_in_m= height * 0.0254
    
    bmi = weight_in_kg/(height_in_m**2)
    
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

BMI_calculator(int(input("Enter weight in pounds:")), int(input("Enter height in inches:")))
        
    
    
