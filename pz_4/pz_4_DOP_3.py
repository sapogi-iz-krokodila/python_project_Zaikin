'''Найти и вывести на экран квадраты и кубы чисел от 2 до 5.'''

number = 2
while number <= 5:
    square = number ** 2
    cube = number ** 3
    print(f"квадрат числа = {square}, куб числа = {cube}")
    number += 1
