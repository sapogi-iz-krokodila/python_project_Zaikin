'''Арифметические действия над числами пронумерованы следующим образом: 1 —
сложение, 2 — вычитание, 3 — умножение, 4 — деление. Дан номер действия N
(целое число в диапазоне 1-4) и вещественные числа A и B (В не равно 0). Выполнить
над числами указанное действие и вывести результат.'''

while True:
    try:
        number = int(input("Введите действия над числами : 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление."))
        if number >= 1 and number <= 4:
            break
        else:
            print("Ошибка: номер должен быть от 1 до 4!")
    except ValueError:
        print("Введите правильное значение")

while True:
    try:
        number_a = float(input("Введите первое вещественное число A: "))
        number_b = float(input("Введите второе вещественное число B (не равное нулю): "))
        if number_b == 0:
            print("ошибка число B не должно ровнятся 0")
        else:
            break
    except ValueError:
        print("Введите правильное значение")

if number == 1:
    print(f"сложение: {number_a + number_b}" )

elif number == 2:
    print(f"вычитание: {number_a - number_b}")

elif number == 3:
    print(f"умножение: {number_a * number_b}")

elif number == 4:
    print(f"деление: {number_a / number_b}")