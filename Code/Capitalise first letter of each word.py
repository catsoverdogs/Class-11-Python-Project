string = input("Enter words: ")
words = string.split()
new_string = ""

for word in words:
    new_string += word.capitalize() + " "

print(new_string.strip())
