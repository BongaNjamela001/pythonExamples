import math
import math

def is_leap(year):
   """Returns True for a leap year and False otherwise"""   
   
   if year%100 == 0:
      leap_mod = year%400
   else:
      leap_mod = year%4
   
   if leap_mod == 0:
      leap = True
   else:
      leap = False
      
   return leap

def month_num(month_name):
   """Returns an integer value for a month,i.e. 1 = Jan,...,12 = December"""
   month1 = month_name.lower()
   
   if month1 == "january":
      m = 1
   elif month1 == "february":
      m = 2
   elif month1 == "march":
      m = 3
   elif month1 == "april":
      m = 4
   elif month1 == "may":
      m = 5
   elif month1 == "june":
      m = 6
   elif month1 == "july":
      m = 7
   elif month1 == "august":
      m = 8
   elif month1 == "september":
      m = 9 
   elif month1 == "october":
      m = 10
   elif month1 == "november":
      m = 11
   else:
      m = 12
   return m

def day_of_week(day, month, year):
   """Uses Zeller's Congruence to return integer value for the day on which a date 
   (in the form d/m/y) falls, i.e. 1 = Mon, ..., 7 = Sun"""  
   week_day = day + math.floor((13*(month+1))/5)
   week_day += (year)
   week_day += math.floor((year)/4) - math.floor((year)/100)
   week_day += math.floor((year)/400)
   week_day %= 7 
   week_day += 5
   week_day %= 7
   week_day += 1      
   
   if month == 1: 
      week_day = day + math.floor((13*((month+12)+1))/5)
      week_day += (year-1)
      week_day += math.floor((year-1)/4) - math.floor((year-1)/100)
      week_day += math.floor((year-1)/400)
      week_day %= 7 
      week_day += 5
      week_day %= 7
      week_day += 1
   
   elif month == 2:
      week_day = day + math.floor((13*((month+12)+1))/5)
      week_day += (year-1)
      week_day += math.floor((year-1)/4) - math.floor((year-1)/100)
      week_day += math.floor((year-1)/400)
      week_day %= 7 
      week_day += 5
      week_day %= 7
      week_day += 1
      
   return week_day

def num_days_in(month_num, year):
   """Given a month, and year, function returns the number of
   days in the month"""
   if month_num == 1:
      num_days = 31
   
   elif month_num == 2:
      leap = is_leap(year)
      if leap == True:
         num_days = 29
      elif leap == False:
         num_days = 28
   
   elif month_num == 3:
      num_days = 31
   
   elif month_num == 4:
      num_days = 30
   
   elif month_num == 5:
      num_days = 31
   
   elif month_num == 6:
      num_days = 30
   
   elif month_num == 7:
      num_days = 31
   
   elif month_num == 8:
      num_days = 31
   
   elif month_num == 9:
      num_days = 30
   
   elif month_num == 10:
      num_days = 31
   
   elif month_num == 11:
      num_days = 30
   
   else:
      num_days = 31
   
   return num_days

def num_weeks(month_num, year):
   """Given an integer representation of a month and a year, function returns
   number of week in that month"""
   first_day_jan  = 1 + 5 * ((year-1)/4)
   first_day_jan += 4 * ((year-1)/100)
   first_day_jan += 6 * ((year-1)/400)
   first_day_jan %= 7
   first_day_jan += 1
   month_length = num_days_in
   num_weeks = 0
   leap = is_leap(year)
   
   if month_num == 1:
      
      if first_day_jan < 6:
         num_weeks = 5
      elif first_day_jan >= 6:
         num_weeks = 6
         
   elif month_num == 2: 
      
      first_day_feb = 1 + math.floor((13*(14+1))/5)
      first_day_feb += (year-1)
      first_day_feb += math.floor((year-1)/4) - math.floor((year-1)/100)
      first_day_feb += math.floor((year-1)/400)
      first_day_feb %= 7
      first_day_feb += 5
      first_day_feb %= 7
      first_day_feb += 1
      leap = is_leap(year)
      
      if leap == True:
         num_weeks = 5
      else:
         if first_day_feb == 1:
            num_weeks = 4
         else:
            num_weeks = 5
   
   elif month_num == 3:
      
      first_day = 1 + math.floor((13*(3+1))/5)
      first_day += year
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
      
      if first_day < 6:
         num_weeks = 5
      elif first_day >= 6:
         num_weeks = 6

   elif month_num == 4:
         
      first_day = 1 + math.floor((13*(4+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
      
      if first_day < 7:
         num_weeks = 5
      elif first_day == 7:
         num_weeks = 6
   
   elif month_num == 5:
         
      first_day = 1 + math.floor((13*(5+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
      
      if first_day < 6:
         num_weeks = 5
      elif first_day >= 6:
         num_weeks = 6
   
   elif month_num == 6:
         
      first_day = 1 + math.floor((13*(6+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 7:
         num_weeks = 5
      elif first_day >= 7:
         num_weeks = 6
   
   elif month_num == 7:
         
      first_day = 1 + math.floor((13*(7+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 6:
         num_weeks = 5
      elif first_day >= 6:
         num_weeks = 6
   
   elif month_num == 8:
         
      first_day = 1 + math.floor((13*(8+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 6:
         num_weeks = 5
      elif first_day >= 6:
         num_weeks = 6
   
   elif month_num == 9:
         
      first_day = 1 + math.floor((13*(9+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 7:
         num_weeks = 5
      elif first_day >= 7:
         num_weeks = 6
   
   elif month_num == 10:
         
      first_day = 1 + math.floor((13*(10+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 6:
         num_weeks = 5
      elif first_day >= 6:
         num_weeks = 6
         
   elif month_num == 11:
         
      first_day = 1 + math.floor((13*(11+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 7:
         num_weeks = 5
      elif first_day >= 7:
         num_weeks = 6
   
   else:
         
      first_day = 1 + math.floor((13*(12+1))/5)
      first_day += (year)
      first_day += math.floor((year)/4) - math.floor((year)/100)
      first_day += math.floor((year)/400)
      first_day %= 7
      first_day += 5
      first_day %= 7
      first_day += 1
         
      if first_day < 6:
         num_weeks = 5
      elif first_day >= 6:
         num_weeks = 6      
   
   return num_weeks


def week(week_num, start_day, days_in_month):
   """Function is used in a 'for' loop in the main function to iterate 
   from 1 to the number of weeks in the month to print out the string 
   rows of the month calendar. For example, week(1,5,2020) gives the string
   "         1  2  3" since the 1/May/2020 was on a friday"""
   if days_in_month == 31: 
      if start_day == 1:
         if week_num == 1:
            print(" 1  2  3  4  5  6  7")
         elif week_num == 2: 
            print(" 8  9 10 11 12 13 14")
         elif week_num == 3:
            print("15 16 17 18 19 20 21")
         elif week_num == 4:  
            print("22 23 24 25 26 27 28")
         else:
            print("29 30 31")
      elif start_day == 2:
         if week_num == 1:
            print("    1  2  3  4  5  6")
         elif week_num == 2: 
            print(" 7  8  9 10 11 12 13")
         elif week_num == 3:     
            print("14 15 16 17 18 19 20")
         elif week_num == 4:
            print("21 22 23 24 25 26 27")
         else:
            print("28 29 30 31")      
      elif start_day == 3:
         if week_num == 1:
            print("       1  2  3  4  5")
         elif week_num == 2: 
            print(" 6  7  8  9 10 11 12")
         elif week_num == 3:
            print("13 14 15 16 17 18 19")
         elif week_num == 4:
            print("20 21 22 23 24 25 26")
         else:
            print("27 28 29 30 31")
      elif start_day == 4:
         if week_num == 1:
            print("          1  2  3  4")
         elif week_num == 2: 
            print(" 5  6  7  8  9 10 11")
         elif week_num == 3:
            print("12 13 14 15 16 17 18")
         elif week_num == 4:
            print("19 20 21 22 23 24 25")
         else: 
            print("26 27 28 29 30 31")
      elif start_day == 5:
         if week_num == 1:
            print("             1  2  3")
         elif week_num == 2: 
            print(" 4  5  6  7  8  9 10")
         elif week_num == 3:
            print("11 12 13 14 15 16 17")
         elif week_num == 4:
            print("18 19 20 21 22 23 24")
         else:
            print("25 26 27 28 29 30 31")
      elif start_day == 6:
         if week_num == 1:
            print("                1  2")
         elif week_num == 2: 
            print(" 3  4  5  6  7  8  9")
         elif week_num == 3:
            print("10 11 12 13 14 15 16")
         elif week_num == 4:
            print("17 18 19 20 21 22 23")
         elif week_num == 5:
            print("24 25 26 27 28 29 30")
         else:
            print("31")
      elif start_day == 7:
         if week_num == 1:
            print("                   1")
         elif week_num == 2: 
            print(" 2  3  4  5  6  7  8")
         elif week_num == 3:
            print(" 9 10 11 12 13 14 15")
         elif week_num == 4:
            print("16 17 18 19 20 21 22")
         elif week_num == 5:
            print("23 24 25 26 27 28 29")
         else:
            print("30 31")
   if days_in_month == 30: 
      if start_day == 1:
         if week_num == 1:
            print(" 1  2  3  4  5  6  7")
         elif week_num == 2: 
            print(" 8  9 10 11 12 13 14")
         elif week_num == 3:
            print("15 16 17 18 19 20 21")
         elif week_num == 4:  
            print("22 23 24 25 26 27 28")
         else:
            print("29 30")
      elif start_day == 2:
         if week_num == 1:
            print("    1  2  3  4  5  6")
         elif week_num == 2: 
            print(" 7  8  9 10 11 12 13")
         elif week_num == 3:     
            print("14 15 16 17 18 19 20")
         elif week_num == 4:
            print("21 22 23 24 25 26 27")
         else:
            print("28 29 30 30")      
      elif start_day == 3:
         if week_num == 1:
            print("       1  2  3  4  5")
         elif week_num == 2: 
            print(" 6  7  8  9 10 11 12")
         elif week_num == 3:
            print("13 14 15 16 17 18 19")
         elif week_num == 4:
            print("20 21 22 23 24 25 26")
         else:
            print("27 28 29 30")
      elif start_day == 4:
         if week_num == 1:
            print("          1  2  3  4")
         elif week_num == 2: 
            print(" 5  6  7  8  9 10 11")
         elif week_num == 3:
            print("12 13 14 15 16 17 18")
         elif week_num == 4:
            print("19 20 21 22 23 24 25")
         else: 
            print("26 27 28 29 30")
      elif start_day == 5:
         if week_num == 1:
            print("             1  2  3")
         elif week_num == 2: 
            print(" 4  5  6  7  8  9 10")
         elif week_num == 3:
            print("11 12 13 14 15 16 17")
         elif week_num == 4:
            print("18 19 20 21 22 23 24")
         else:
            print("25 26 27 28 29 30")
      elif start_day == 6:
         if week_num == 1:
            print("                1  2")
         elif week_num == 2: 
            print(" 3  4  5  6  7  8  9")
         elif week_num == 3:
            print("10 11 12 13 14 15 16")
         elif week_num == 4:
            print("17 18 19 20 21 22 23")
         else:
            print("24 25 26 27 28 29 30")
      elif start_day == 7:
         if week_num == 1:
            print("                   1")
         elif week_num == 2: 
            print(" 2  3  4  5  6  7  8")
         elif week_num == 3:
            print(" 9 10 11 12 13 14 15")
         elif week_num == 4:
            print("16 17 18 19 20 21 22")
         elif week_num == 5:
            print("23 24 25 26 27 28 29")
         else:
            print("30")
   if days_in_month == 28: 
      if start_day == 1:
         if week_num == 1:
            print(" 1  2  3  4  5  6  7")
         elif week_num == 2: 
            print(" 8  9 10 11 12 13 14")
         elif week_num == 3:
            print("15 16 17 18 19 20 21")
         else:  
            print("22 23 24 25 26 27 28")         
      elif start_day == 2:
         if week_num == 1: 
            print("    1  2  3  4  5  6")
         elif week_num == 2: 
            print(" 7  8  9 10 11 12 13")
         elif week_num == 3:     
            print("14 15 16 17 18 19 20")
         elif week_num == 4:
            print("21 22 23 24 25 26 27")
         else:
            print("28")      
      elif start_day == 3:
         if week_num == 1:
            print("       1  2  3  4  5")
         elif week_num == 2: 
            print(" 6  7  8  9 10 11 12")
         elif week_num == 3:
            print("13 14 15 16 17 18 19")
         elif week_num == 4:
            print("20 21 22 23 24 25 26")
         else:
            print("27 28")
      elif start_day == 4:
         if week_num == 1:
            print("          1  2  3  4")
         elif week_num == 2: 
            print(" 5  6  7  8  9 10 11")
         elif week_num == 3:
            print("12 13 14 15 16 17 18")
         elif week_num == 4:
            print("19 20 21 22 23 24 25")
         else: 
            print("26 27 28")
      elif start_day == 5:
         if week_num == 1:
            print("             1  2  3")
         elif week_num == 2: 
            print(" 4  5  6  7  8  9 10")
         elif week_num == 3:
            print("11 12 13 14 15 16 17")
         elif week_num == 4:
            print("18 19 20 21 22 23 24")
         else:
            print("25 26 27 28")
      elif start_day == 6:
         if week_num == 1:
            print("                1  2")
         elif week_num == 2: 
            print(" 3  4  5  6  7  8  9")
         elif week_num == 3:
            print("10 11 12 13 14 15 16")
         elif week_num == 4:
            print("17 18 19 20 21 22 23")
         else:
            print("24 25 26 27 28")
      elif start_day == 7:
         if week_num == 1:
            print("                   1")
         elif week_num == 2: 
            print(" 2  3  4  5  6  7  8")
         elif week_num == 3:
            print(" 9 10 11 12 13 14 15")
         elif week_num == 4:
            print("16 17 18 19 20 21 22")
         else:
            print("23 24 25 26 27 28")
   if days_in_month == 29: 
      if start_day == 1:
         if week_num == 1:
            print(" 1  2  3  4  5  6  7")
         elif week_num == 2: 
            print(" 8  9 10 11 12 13 14")
         elif week_num == 3:
            print("15 16 17 18 19 20 21")
         elif week_num == 4:  
            print("22 23 24 25 26 27 28")
         else:
            print("29")
      elif start_day == 2:
         if week_num == 1:
            print("    1  2  3  4  5  6")
         elif week_num == 2: 
            print(" 7  8  9 10 11 12 13")
         elif week_num == 3:     
            print("14 15 16 17 18 19 20")
         elif week_num == 4:
            print("21 22 23 24 25 26 27")
         else:
            print("28 29")      
      elif start_day == 3:
         if week_num == 1:
            print("       1  2  3  4  5")
         elif week_num == 2: 
            print(" 6  7  8  9 10 11 12")
         elif week_num == 3:
            print("13 14 15 16 17 18 19")
         elif week_num == 4:
            print("20 21 22 23 24 25 26")
         else:
            print("27 28")
      elif start_day == 4:
         if week_num == 1:
            print("          1  2  3  4")
         elif week_num == 2: 
            print(" 5  6  7  8  9 10 11")
         elif week_num == 3:
            print("12 13 14 15 16 17 18")
         elif week_num == 4:
            print("19 20 21 22 23 24 25")
         else: 
            print("26 27 28 29")
      elif start_day == 5:
         if week_num == 1:
            print("             1  2  3")
         elif week_num == 2: 
            print(" 4  5  6  7  8  9 10")
         elif week_num == 3:
            print("11 12 13 14 15 16 17")
         elif week_num == 4:
            print("18 19 20 21 22 23 24")
         else:
            print("25 26 27 28 29")
      elif start_day == 6:
         if week_num == 1:
            print("                1  2")
         elif week_num == 2: 
            print(" 3  4  5  6  7  8  9")
         elif week_num == 3:
            print("10 11 12 13 14 15 16")
         elif week_num == 4:
            print("17 18 19 20 21 22 23")
         else:
            print("24 25 26 27 28 29")
      elif start_day == 7:
         if week_num == 1:
            print("                   1")
         elif week_num == 2: 
            print(" 2  3  4  5  6  7  8")
         elif week_num == 3:
            print(" 9 10 11 12 13 14 15")
         elif week_num == 4:
            print("16 17 18 19 20 21 22")
         else:
            print("23 24 25 26 27 28 29")
           
def main():
   
   month_ = input("Enter month:\n")
   year_ = eval(input("Enter year:\n"))
   
   leap_bool = is_leap(year_) #assigning True for leap year or False to nonleap
   month_1 = month_[:1] #Ensuring that the first letter of month is a capital
   month_2 = month_1.upper()
   month_3 = month_.lower()
   month_4 = month_3[1:]
   
   m = month_num(month_) #assign integer value to month name
   month_length = num_days_in(m, year_) #assign number of days in month
   start_day1 = day_of_week(1, m, year_) #assign first day on year
   
   week_num1 = num_weeks(m, year_) #assign number of weeks in month
   
   print(month_2, end="")
   print(month_4)
   print("Mo Tu We Th Fr Sa Su")
   
   for week_number in range(1,week_num1+1): #prints out 
      week(week_number, start_day1, month_length)
   print()      
if __name__== '__main__':
   main()






