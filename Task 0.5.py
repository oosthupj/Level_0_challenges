def area_of_triangle(x,y,z):
    semiperimeter  = 0.5*int(x+y+z) 
    area = semiperimeter*((semiperimeter - x)*(semiperimeter - y)*(semiperimeter - z)) 
    print(area**(1/2)) 

area_of_triangle(3,4,5)
area_of_triangle(6,5,5)