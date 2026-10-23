'''Дано число A (> 1). Вывести наименьшее из целых чисел K, для которых сумма 1 +
1/2 + ... + 1/K будет больше A, и саму эту сумму.'''

while True:
    try:
        number_a = float(input("Введите число A > 1: "))
        if number_a <= 1:
            print("Введите корректное значение, оно должно соответствовать условию A > 1")
        else:
            break
    except ValueError:
        print("Введите корректное значение")

k = 0
total_sum = 0.0

while total_sum <= number_a:
    k += 1
    total_sum += 1 / k

print(f"Наименьшее число K: {k}")
print(f"Сумма: {total_sum}")