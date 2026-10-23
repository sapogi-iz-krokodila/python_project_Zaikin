'''Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).'''

number = int(input("Введите число n > 1 "))

total_sum = 0
factorial = 1
i = 1

while i <= number:
    factorial *= i
    total_sum += factorial
    i += 1
print(f"факториал числа {number} равен {total_sum}")