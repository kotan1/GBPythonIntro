a = float(input("Enter first distance: "))
b = float(input("Enter second distance: "))

days = 1

while a < b:
    days += 1
    a *= 1.1

print(days)