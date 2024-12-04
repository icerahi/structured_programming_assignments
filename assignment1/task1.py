"""  
Currency Conversion

Convert an amount in US dollars to various foreign currencies. 
Write a program that reads an amount in US dollars and converts it to euros, yen, 
and pounds using the following conversion rates:

1 USD = 0.85 Euros
1 USD = 109.57 Yen
1 USD = 0.73 Pounds
The program should output the equivalent amount in each currency.
"""

def conversion(usd):
    euro=0.85*usd 
    yen=109.57*usd 
    pounds=0.73*usd 
    print(f"{usd} USD = {euro} EUR \n{usd} USD = {yen} YEN \n{usd} USD = {pounds} POUNDS")
    
conversion(int(input("Enter the amount in USD:")))