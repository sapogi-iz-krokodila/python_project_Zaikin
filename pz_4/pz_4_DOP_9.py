'''Посчитать и вывести количество элементов арифметической прогрессии,
удовлетворяющих условию 10<ai<30.'''

number = int(input("Введите количество элементов прогрессии: "))

current_element = 1
count = 0
i = 1

while i <= number:
    if 10 < current_element < 30:
        count += 1
    current_element += 3
    i += 1

print(count)