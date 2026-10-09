''' Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
случае увеличить его в 1.5 раза.'''

number_a = int(input("Введите число A: "))
number_b = int(input("Введите число B: "))

result = number_a * number_b
if result < 0:
      multiplication_result = result * 8
      print(f"{multiplication_result}")

else:
    multiplication = result * 1.5
    print(f"{multiplication}")




