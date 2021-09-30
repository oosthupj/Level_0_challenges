def area_of_triangle(x,y,z):
    """ semiperimeter formula """
    s = 0.5*int(x+y+z) 
    """ area from semiperimeter formula part 1 """
    a = 6*((s-x)*(s-y)*(s-z)) 
    """   area from semiperimeter formula part 1 """
    print(a**(1/2)) 

area_of_triangle(3,4,5)