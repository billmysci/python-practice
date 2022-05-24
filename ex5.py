name = 'Branden J. Williams'
age = 20 # not a lie
height = 70.0 # inches
weight = 120.0 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

# converting imperial units to metric
met_weight = weight / 2.205
met_height = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That's also {met_height} centimeters.")
print(f"He's {weight} pounds heavy.")
print(f"That's also {met_weight} kilograms.")
print("Actually, that's pretty light.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

