
def get_block(data):
   """This function extracts the block string from the
   raw data"""
   start = data.find("BEGIN") 
   end = data.find("END") + 3
   block = data[start:end] 
   return block

def location(block):
   """Prints the location which is reversed in the data string"""
   temp_block = block
   end = temp_block.find("END") - len(" ")
   start = temp_block.find(":")+13
   reversed_str = temp_block[start:end]
   first_caps = len(reversed_str) - 1
   first_caps_alpha = reversed_str[first_caps]
   second_caps = reversed_str.find(" ") - 1
   second_caps_ = reversed_str[second_caps]
   second_capital = second_caps_.upper()
   lower_cases = reversed_str.lower()
   for position in range(len(reversed_str)-2,-1,-1):
      if position == second_caps:
         continue
      else:
         lower = lower_cases[position]
      location = first_caps_alpha+lower+" "+second_capital
   
   return location
   
def temperature(block):
   """Extracts the temperature from the data block"""
   temp_block = block
   start = temp_block.find("BEGIN")+len("BEGIN ")
   end = temp_block.find("_")
   temp = eval(temp_block[start:end])
   return temp
   
def x_coordinate(block):
   """Extracts the x coordinate of the location from data block"""
   temp_block = block     
   start = temp_block.find(":")+1 
   end = temp_block.find(",") 
   x_coordinate = temp_block[start:end]
   return x_coordinate

def y_coordinate(block):
   """Extracts the y coordinate of the location from data block"""
       
   temp_block = block
   start = temp_block.find(",")+1 
   end = temp_block.find(",")+6
   y_coordinate = temp_block[start:end]
   return y_coordinate

def pressure(block):
   """Extracts the pressure from the data block""" 
   temp_block = block     
   start = temp_block.find("_")+1
   end = temp_block.find(":")
   return eval(temp_block[start:end]) 

def main():
   data = input('Enter the raw data:\n')
   block = get_block(data)
   print('Site information:')
   print('Location:', location(block)) 
   print('Coordinates:', y_coordinate(block), x_coordinate(block))
   print('Temperature: {:.2f} C'.format(temperature(block)))
   print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
   main()
