def number_to_hrs_mns(number):
    hour = number/60
    hour = int(hour)
    minutes = number%60 
    strhr = " hour"
    strmin = " minute"
    
    if hour>1:
        strhr = " hours"
    if minutes>1:
        strmin = " minutes"

    print(str(hour) + strhr +", " + str(minutes) + strmin)

number_to_hrs_mns(71)
number_to_hrs_mns(133)
number_to_hrs_mns(61)

