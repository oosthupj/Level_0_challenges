def number_to_hours_minutes(number):
    hour = number/60
    hour = int(hour)
    minutes = number%60 
    string_hour = " hour"
    string_minute = " minute"
    
    if hour>1:
        string_hour = " hours"
    if minutes>1:
        string_minute = " minutes"

    return(str(hour) + string_hour +", " + str(minutes) + string_minute)

""" 
This is just to test the function
"""
print(number_to_hours_minutes(71))
print(number_to_hours_minutes(133))
print(number_to_hours_minutes(61))

