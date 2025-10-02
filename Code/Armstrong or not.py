n = int(input("Enter number: "))
temp = n
total = 0
digits = len(str(n))

while temp:
    total += (temp % 10) ** digits
    temp //= 10

print("Armstrong" if total == n else "Not Armstrong")
