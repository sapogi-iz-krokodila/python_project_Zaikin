'''Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
в противном случае уменьшить на 2.'''

number_a = int(input("Введите двузначное число"))
summ = ((number_a // 10) + (number_a % 10))

if summ % 2 == 0:
    increase = number_a + 2
    print(f"{increase}")
else:
    decrease = number_a - 2
    print(f"{decrease}")