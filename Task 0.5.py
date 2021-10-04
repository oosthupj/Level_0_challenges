def area_of_triangle(x,y,z):
    semiperimeter  = 0.5*int(x+y+z) 
    area = semiperimeter*((semiperimeter - x)*(semiperimeter - y)*(semiperimeter - z)) 
    return(area**(1/2)) 

'''
This is just to test the funcion
'''
print(area_of_triangle(3,4,5))
print(area_of_triangle(6,5,5))