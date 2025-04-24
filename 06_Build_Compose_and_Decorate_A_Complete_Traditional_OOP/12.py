# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

# class TemperatureConverter
class TemperatureConverter:
    def __init__(self, temperature):
        self.temperature = temperature

    # Static method
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Formula
        return (c * 9/5) + 32
    
# Initialize value
celcius = 32
# storing data
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celcius)
# printing data
print(f"{celcius}°C is equal to {fahrenheit}°F")

# Output: 32°C is equal to 89.6°F