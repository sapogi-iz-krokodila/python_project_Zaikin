''''Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.'''

number_a = int(input("Введите число"))

if number_a % 2 == 0:
    proverka_result = number_a // 4
    print(f"{proverka_result}")
else:
    proverka_result_2 = number_a * 5
    print(f"{proverka_result_2}")