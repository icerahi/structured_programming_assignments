#Task 5: Distance Conversion


def distance_converter(km):
    miles=km*0.621371
    feet= miles * 5280
    inches= feet *12
    
    print(f"{km} equal to:\n{miles} miles. \n{feet} Feet.\n{inches} Inches.")
    
distance_converter(int(input('Enter distance in KM:')))