string = input("Enter a string: ")
swapped = ""

for ch in string:
    if ch.isupper():
        swapped += ch.lower()
    elif ch.islower():
        swapped += ch.upper()
    else:
        swapped += ch

print(swapped)
