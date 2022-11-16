# This program takes a year range from the user and prints out the day..
# ...on which the first of January falls on each year
# bonga njamela
# njmlun002
# 29 February 2020

year_1 = eval(input("Enter the first year:\n"))
year_2 = eval(input("Enter the second year:\n"))

for i in range(year_1, year_2+1):
    day = 1 + 5 * ((i-1)%4)
    day += 4 * ((i-1)%100)
    day += 6 * ((i-1)%400)
    day %= 7
    if day == 0:
        day = "Sunday"
        print("The 1st of January", i, end="")
        print(" falls on a", day, end="")
        print(".")
    else:
        if day == 1:
            day = "Monday"
            print("The 1st of January", i, end="")
            print(" falls on a", day, end="")
            print(".")
        else:
            if day == 2:
                day = "Tuesday"
                print("The 1st of January", i, end="")
                print(" falls on a", day, end="")
                print(".")
            else:
                if day == 3:
                    day = "Wednesday"
                    print("The 1st of January", i, end="")
                    print(" falls on a", day, end="")
                    print(".")
                else:
                    if day == 4:
                        day = "Thursday"
                        print("The 1st of January", i, end="")
                        print(" falls on a", day, end="")
                        print(".")
                    else:
                        if day == 5:
                            day = "Friday"
                            print("The 1st of January", i, end="")
                            print(" falls on a", day, end="")
                            print(".")
                        else:
                            if day == 6:
                                day = "Saturday"
                                print("The 1st of January", i, end="")
                                print(" falls on a", day, end="")
                                print(".")                                
            
    