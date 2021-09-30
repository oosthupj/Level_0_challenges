def area_of_triangle(x,y,z):
    s = 0.5*int(x+y+z) #semiperimeter formula
    a = 6*((s-x)*(s-y)*(s-z)) #area from semiperimeter formula part 1
    print(a**(1/2)) #area from semiperimeter formula part 1

area_of_triangle(3,4,5)