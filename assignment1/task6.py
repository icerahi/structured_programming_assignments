#Task 6: Time Conversion

from datetime import timedelta

def days_hours_minutes(min):
    td=timedelta(minutes=min)
    days= td.days
    hours= td.seconds//3600
    minutes= td.seconds//60
    print(f"{days} Days,{hours} hours,{minutes} minutes.")
    
    
days_hours_minutes(int(input("Enter time duration in minutes:")))