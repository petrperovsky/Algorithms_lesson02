chet = 0
nechet = 0

n = int(input("Введите натуральное число: "))

while True:
    if n % 10 % 2 == 0:
        chet += 1
    else:
        nechet += 1
    n //= 10
    if not n:
        break

print(f"четных: {chet}, нечетных: {nechet}")
