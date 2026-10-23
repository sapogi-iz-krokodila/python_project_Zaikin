'''Ввести N чисел. Найти и вывести их среднее арифметическое.'''

numbers = int(input("Введите количество чисел N:"))

total_sum = 0.0
i = 0

while i <= numbers:
    number = float(input("Введите число N:"))
    total_sum += number
    i += 1

division = total_sum / numbers
print(f"серднеарифметическое = {division}")