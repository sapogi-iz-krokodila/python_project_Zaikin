'''Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.'''
number_a = int(input("Введите число A "))
number_b = int(input("Введите число B "))

summ = number_a + number_b

if (summ % 5) == 0:
    increase = summ + 1
    print(f"{increase}")
else:
    decrease = summ - 2
    print(f"{decrease}")