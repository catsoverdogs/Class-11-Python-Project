import math

x = float(input("Enter x: "))
n = int(input("Enter n: "))

# Series 1: 1 + x + x^2 + ... + x^n
if x == 1:
    sum1 = n + 1
else:
    sum1 = (x**(n + 1) - 1) / (x - 1) 
print(f"Series 1 Sum: {sum1}")

# Series 2: 1 - x + x^2 - x^3 + ... 
if x == -1:
    sum2 = (n + 1) / 2 if (n + 1) % 2 == 0 else 0.5
else:
    common_ratio = -x
    sum2 = (common_ratio**(n + 1) - 1) / (common_ratio - 1)
print(f"Series 2 Sum: {sum2}")

# Series 3: x + x^2/2 + x^3/3 + ... + x^n/n
sum3 = 0.0
for i in range(1, n + 1):
    sum3 += (x ** i) / i
print(f"Series 3 Sum: {sum3}")

# Series 4: x + x^2/2! + x^3/3! + ... + x^n/n!
sum4 = 0.0
for i in range(1, n + 1):
    sum4 += (x ** i) / math.factorial(i)
print(f"Series 4 Sum: {sum4}")
