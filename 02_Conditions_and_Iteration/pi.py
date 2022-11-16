# This program approximates the value of pi and calculates area of a circle 
# whose radius is in requested from the user
# bonga njamela
# njmlun002
# 29 February 2020

from math import sqrt

initial_term = 2*(2/sqrt(2))
denom_root = sqrt(2)
pi = initial_term

while 2/sqrt(2+denom_root) > 1:
    pi *= 2/sqrt(2+denom_root)
    denom_root = sqrt(2+denom_root)
rounded_pi = round(pi,3)
print("Approximation of pi:", rounded_pi)

circle_radius = eval(input("Enter the radius:\n"))
circle_area = pi*circle_radius**2
circle_area = round(circle_area,3)
print("Area:", circle_area)

    
    