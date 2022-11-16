# program simulates a vending machine change calculator
# bonga njamela
# 14 March 2020

cost = eval(input("Enter the cost (in Rand):\n"))
deposit = eval(input("Deposit a coin or note (in Rand):\n"))
initial_change = cost - deposit

if initial_change == 0:
        print("You have paid the full amount. Thank you.")
elif initial_change == 10:
        print("Your change is:\n")
        print("1 x R10")
elif initial_change == 20:
        print("Your change is:\n")
        print("1 x R20")
elif initial_change == 50:
        print("Your change is:\n")
        print("1 x R50")

else:
        while deposit - cost < 0:
                new_deposit = eval(input("Deposit a coin or note (in Rand):\n"))
                deposit += new_deposit
        
        change = deposit - cost
        req_notes = change - change%10
        
        print("Your change is:")
        if req_notes == 90:
                print("1 x R50")
                print("2 x R20")
        elif req_notes == 80:
                print("1 x R50")
                print("1 x R20")
                print("1 x R10")
        elif req_notes == 70:     
                print("1 x R50")
                print("1 x R20")      
        elif req_notes == 60:
                print("1 x R50")
                print("1 x R10")
        elif req_notes == 50:
                print("1 x R50")
        elif req_notes == 40:     
                print("2 x R20")       
        elif req_notes == 30:     
                print("1 x R20")
                print("1 x R30")
        elif req_notes == 20:
                print("1 x R20")
        elif req_notes == 10:
                print("1 x R10")
        
        if change == 0:
                print("You have paid the full amount. Thank you.")
        elif change%10 >= 5:
                if change%10 == 5:
                        print("1 x R5")
                elif change%10 == 6:
                        print("1 x R5")
                        print("1 x R1")
                elif change%10 == 7:
                        print("1 x R5")
                        print("1 x R2")
                elif change%10 == 8:
                        print("1 x R5")
                        print("1 x R2")
                        print("1 x R1")
                elif change%10 == 9:
                        print("1 x R5")
                        print("2 x R2")
        elif change%10 < 5:
                if change%10 == 1:
                        print("1 x R1")
                elif change%10 == 2:
                        print("1 x R2")
                elif change%10 == 3:
                        print("1 x R1")
                        print("1 x R2")
                elif change%10 == 4:
                        print("2 x R2")
                
                
                        
                                
                                
                        
                
             