# imports arguments into the file
from sys import argv

# adds 2 arguments
script, filename = argv

# defines variable txt to open file in argument
txt = open(filename)

# prints the name of the file in argument
print(f"Here's your file {filename}:")
# prints the opened file's content
print(txt.read())

# prints a string that prompts the user to type the filename again
print("Type the filename again:")
# creates variable with user input prompt
file_again = input("> ")

# creates variable that opens filename in user input
txt_again = open(file_again)

# prints newly opened file
print(txt_again.read())

txt.close();txt_again.close()