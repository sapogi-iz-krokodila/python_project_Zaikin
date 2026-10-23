'''Ввести 4 числа. Найти и вывести на экран количество четных чисел.'''

neg_summ = 0.0
neg_count = 0
i = 1

while i <= 4:
    number_i = int(input("Введите число "))
    if number_i % 2 == 0:
        neg_summ += number_i
        neg_count += 1
    i += 1

print(neg_summ)
print(neg_count)

