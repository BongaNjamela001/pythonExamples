# This program accepts a temperature given in Fahrenheit and 
# prints the equivalent in Celsius and in Kelvin.
# Name: Stephan Jamieson
# 27th February 2017
#
input_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit_value = eval(input_str)

# Calculate equivalent Celsius value
celsius_value = (fahrenheit_value - 32)*(5/9) 

# Calculate equivalent Kelvin value
kelvin_value = celsius_value+273.15

print("The temperature in Celsius is:", celsius_value)
print("The temperature in Kelvin is:", kelvin_value) 