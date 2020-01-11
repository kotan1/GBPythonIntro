num = int(input("Enter a number: "))

max = num % 10
num //= 10

while num > 0:
    if num % 10 > max:
        max = num % 10

    num //= 10

print(max)