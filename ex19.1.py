def number_function(first_number, second_number):
    print(f"First number: {first_number}")
    print(f"Second number: {second_number}\n")

print("1. This function prints numbers.")
number_function(10, 20)

print("2. This is with variables.")

num1 = 50
num2 = 3

number_function(num1, num2)

print("3. This is with math.")
number_function(48 + 239, 4 / 3)

print("4. This is a variable math combo.")
number_function(num1 + 42, num2 + 99)

print("5. This is with 2 inputs.")
number_function(input("Type a number: "),input("Type a second number: "))

print("6. This is with an input and a number.")
number_function(input("Type a number: "), 67)

print("7. This is with an input and a variable.")
number_function(num1, input("Type number 2: "))

print("8. This is with an input and math.")
number_function(input("Type the first number: "), 629 + 582)

print("9. This is with an input, a variable and math.")
number_function(input("Type another number: "), num2 - 10)

print("10. This is with 4 inputs being added as math.")
number_function(int(input("Type this first number: ")) + int(input("Type another number: ")), int(input("Type a third number: ")) + int(input("Type a final number: ")))