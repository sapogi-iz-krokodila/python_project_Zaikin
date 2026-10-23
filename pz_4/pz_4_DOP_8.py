'''Даны два целых числа А и В ($A < B$).
 Найти сумму всех целых чисел от А до В включительно (использовать оператор цикла)'''

number_a = int(input("Введите число А: "))
number_b = int(input("Введите число B > A: "))

total_sum = 0

while number_a <= number_b:
    total_sum += number_a
    number_a += 1

print(total_sum)