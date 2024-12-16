#Task 7: Loan Payment Calculator

def loan_payment(loan_amount:int,interest_rate:float,loan_term:int):
    r= (interest_rate/100)/12
    n= loan_term*12
    p=loan_amount
    
    payment=(p*r*((1+r)**n))/(((1+r)**n)-1)
    print(f"Monthly Payment: {payment}")
    
loan_payment(int(input("Loan amount:")),float(input("interest rate:")),int(input("loan terms:")))