# This program asks the user for a function f(x) and prints out the graph...
# ..as text
# Bonga Njamela
# 9 March 2020

import math 

fnctn = input("Enter a function f(x):\n")

for row in range(10,-11,-1):
    if row != 0:
        for x_var in range(-10,11):
            var_str = fnctn.replace("x", str("(x_var)"))
            y_value = int(eval(var_str))
        
            if y_value == row:
                print("o", end="")  
        
            elif x_var == 0:
                print("|", end="")
                    
            else:
                print(" ", end="")
        print()    
    
    else:
        for x_axis in range(-10,11):
            var_str = fnctn.replace("x", str("(x_axis)"))
            y_value = int(eval(var_str))                
            if y_value == 0:
                print("o", end="")
            elif x_axis == 0:
                print("+",end="")
            else:
                print("-", end="")
        print()
        
        