""" 
Task 4: Temperature Conversion
"""

def temp_converter(fahren):
    celsius= 5/9*(fahren-32)
    kelvin= celsius + 273.15
    
    print(f"{fahren} F:\n{celsius:.2f}C \n{kelvin:.2f}K")
    

temp_converter(int(input("Enter temparature in Fahrenheit:")))