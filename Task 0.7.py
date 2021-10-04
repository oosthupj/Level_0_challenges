def celcius_to_fahrenheit(celcius):
    fahrenheit=(celcius*1.8) + 32
    return(fahrenheit)

celcius_to_fahrenheit(40)

def fahrenheit_to_celcius(fahrenheit):
    celcius=(fahrenheit - 32)/1.8
    return(celcius)

'''
This is just to test the funcions
'''
print(fahrenheit_to_celcius(104))
print(celcius_to_fahrenheit(-32))