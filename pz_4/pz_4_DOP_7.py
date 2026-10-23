'''Даны два целых числа A и B ($A < B$). Вывести в порядке убывания все целые числа,
расположенные между A и B (включая сами числа A и B),
а также количество этих чисел (использовать оператор цикла).'''

number_a = int(input("Введите число А: "))
number_b = int(input("Введите число B > A: "))

count = 0
current = number_b

while current >= number_a:
    print(current)
    current -= 1
    count += 1

print(f"Количество чисел: {count}")