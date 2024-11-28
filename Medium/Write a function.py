# This function checks if a given year is a leap year based on the Gregorian calendar rules.
# It returns True if the year is a leap year, otherwise returns False.

def is_leap(year):
    leap = False
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                leap=True 
        else: leap=True              
    
    return leap
