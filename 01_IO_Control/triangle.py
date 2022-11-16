# The purpose of this program is to give the area of a triangle with 
# dimensions specified by the user
# bonga njamela
# 21 February 2020

# To use the square root we call this function from the math module
from math import sqrt

side_1 = eval(input("Enter the length of the first side: "))
side_2 = eval(input("Enter the length of the second side: "))
side_3 = eval(input("Enter the length of the third side: "))

s = (side_1 + side_2 + side_3)/2

area = sqrt((s*(s-side_1)*(s-side_2)*(s-side_3)))

print("The area of the triangle with sides of length", side_1, end=" and ")
print(side_2, side_3, sep=" and ", end=" ")
print("is", area, end=".")