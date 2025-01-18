#1. Digital Clock Simulation

import time 

def display_time(hours,minutes,seconds):
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
    
def digital_clock():
    hours=0
    minutes=0
    seconds=0
    while True:
        display_time(hours,minutes,seconds)
        time.sleep(1)
        seconds+=1
        
        if seconds==60:
            seconds=0
            minutes+=1
        
        if minutes==60:
            minutes=0
            hours+=1
        
digital_clock()