"""
Fuel Efficiency Calculator

Fuel efficiency in automobiles is often measured in miles per gallon (MPG) in the US.
In Europe, it is commonly measured in liters per 100 kilometers (L/100km).
Write a program that converts fuel efficiency from MPG to L/100km.

The conversion formula is:

L/100km=235.215/MPG

Input the MPG and output the corresponding fuel efficiency in 
"""

def mpg_to_liter_per_100km(mpg):
    
    l_per_100km=235.215/mpg 
    
    print(f"{mpg} MPG = {l_per_100km} liters per 100km")
    
    
mpg_to_liter_per_100km(int(input("Enter Fuel efficiency in MPG:")))