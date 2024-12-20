from Fah_Cel.FtoC import fahrenheit_to_celsius
from Cel_Fah.CtoF import celsius_to_fahrenheit

def main():
    
    
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter choice: ")

    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius: ", celsius)
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit: ", fahrenheit)
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        
if __name__ == "__main__":
    main()
