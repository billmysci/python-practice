# defines a variable with a string
formatter = "{} {} {} {}"

# takes the variable and formats it as integer numbers
print(formatter.format(1, 2, 3, 4))
# takes the variable and formats it as string numbers
print(formatter.format("one", "two", "three", "four"))
# takes the variable and formats it as boolean val
print(formatter.format(True, False, True, False))
# takes the variable and prints it 4 times without values
print(formatter.format(formatter, formatter, formatter, formatter))
# takes the variable and formats it as a poem
print(formatter.format(
    "Triplets born",
    "The throne awaits",
    "A seer warns",
    "of a deadly fate"
))