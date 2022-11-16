# This program checks whether time from a user is correct
# bonga njamela
# njmlun002
# 20 February 2020

hours = eval(input("Enter the hours: "))
minutes = eval(input("Enter the minutes: "))
seconds = eval(input("Enter the seconds: "))

if 0 <= hours <= 23:    # Open primary nest to test if 
    if 0 <= minutes <= 59:  # Open secondary nest when primary nest is true
        if 0 <= seconds <= 59: # Open tertiary if when secondary nest is true
            print("Your time is valid.")
        else:   # Terminate tertiary if when tertiary if is not true
            print("Your time is invalid.") 
    else:   # Terminate secondary nest when secondary nest is false
        print("Your time is invalid.") 
else:   # Terminate primary nest when primary nest is false
    print("Your time is invalid.")