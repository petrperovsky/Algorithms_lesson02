rev = ''
n = int(input("Введите натуральное число: "))

while True:
    rev += str(n % 10)
    n //= 10
    if n == 0:
        break

print(f"Число задом наперед = {rev}")
