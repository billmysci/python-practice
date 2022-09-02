from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is the requested file, {filename}")
print(txt.read())