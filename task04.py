summa = 0

n = int(input("Введите количество суммируемых элементов: "))

if n == 0:
    summa = 0
else:
    for i in range(n):
        summa += (1 / (-2 ** i))

print(f"Сумма ряда = {summa:.6f}")
