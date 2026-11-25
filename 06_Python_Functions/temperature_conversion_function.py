# Topic 6, Task 3: Temperature Conversion Function

def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit: F = (C x 9/5) + 32."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsius = float(input("Enter temperature in Celsius: "))
result = convert_temperature(celsius)
print(f"{celsius:.2f} C = {result:.2f} F")