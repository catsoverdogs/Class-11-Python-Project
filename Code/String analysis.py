string = input("Enter a string: ")

vowels = consonants = uppercase = lowercase = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    if ch.isupper():
        uppercase += 1
    if ch.islower():
        lowercase += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
