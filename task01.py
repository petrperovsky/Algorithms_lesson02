while True:
    a = float(input('Ведите первое число: '))
    b = float(input('Ведите второе число: '))
    operator = input('Ведите оператор + - / *, или 0 для выхода: ')
    if operator == "0":
        break

    elif operator == '+':
        res = a + b
    elif operator == '-':
        res = a - b
    elif operator == '*':
        res = a * b
    elif operator == '/':
        if b == 0:
            print("деление на ноль запрещено, повторите ввод")
            continue
        res = a / b

    else:
        print('Неизвестный оператор')
        continue

    print(f"{a} {operator} {b} = {res}")
