n = int(input("Enter an integer (>1000): "))
if n > 1000:
    rev = int(str(n)[::-1])
    print("Reversed number:", rev)
else:
    print("Number must be greater than 1000")
