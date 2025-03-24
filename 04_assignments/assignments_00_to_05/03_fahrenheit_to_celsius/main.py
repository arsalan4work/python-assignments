def fahrenheit_to_celcius():
    print("This program converts fahrenheit to celcius")
    degree_fahrenheit:float = float(input("Enter temperature in Fahrenheit: "))
    degree_celcius = (degree_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature {degree_fahrenheit}°F = {degree_celcius}°C")



if __name__ == '__main__':
    fahrenheit_to_celcius()