def km_to_miles(km):
    return km * 0.621371

def kg_to_lbs(kg):
    return kg * 2.20462

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

km = float(input("Enter distance in kilometres: "))
print(f"{km} km = {km_to_miles(km):.2f} miles")

kg = float(input("Enter weight in kilograms: "))
print(f"{kg} kg = {kg_to_lbs(kg):.2f} lbs")

c = float(input("Enter temperature in Celsius: "))
print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
