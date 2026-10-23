'''Ввести N чисел. Посчитать и вывести количество чисел равных нулю'''

numbers = int(input("Введите количество чисел N: "))

zero_count = 0
i = 1

while i <= numbers:
    number = int(input("Введите число: "))
    if number == 0:
        zero_count += 1
    i += 1

print(f"Количество чисел равных 0 {zero_count}")