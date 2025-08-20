# Program using functon to convert fahrenheit to celsius

# F = (9/5 × C) + 32
# C = 5 *(F-32)/9

def fah_to_celsius(farenheit):
    celsius = 5 * (farenheit-32)/9 
    return celsius   

farenheit = float(input("Enter temperature in farenheit: "))
print(f"The temperature in farenheit is {fah_to_celsius(farenheit)}")        

# .................................................................

# Program using functon to convert celsius to fahrenheit.
# F = (9/5 × C) + 32

def celsius_to_fah(celsius):
    farenheit = (9/5 * celsius) + 32
    return farenheit    

celsius= float(input("Enter temperature in celsius: ")) 
print(f"The temperature in celsius is {celsius_to_fah(celsius)}")
# The function will prompt the user to input three numbers and determine the greatest among them.