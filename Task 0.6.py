
def get_maximum(a,b,c):
    
    a_is_bigger=False
    b_is_bigger=False
    c_is_bigger=False
    if a>=b:
        a_is_bigger=True 
    if b>a: 
        b_is_bigger= True
    
    if a_is_bigger and c>=a:
        c_is_bigger=True
        a_is_bigger = False
    if b_is_bigger and c>=b:
        c_is_bigger=True
        b_is_bigger=False

    if a_is_bigger:
        return(a)
    elif b_is_bigger:
        return(b)
    elif c_is_bigger:
        return(c)
 

""" This is just to test the function
"""

print(get_maximum(1,2,9))
print(get_maximum(1,1,0))
print(get_maximum(-1,-1,-2))