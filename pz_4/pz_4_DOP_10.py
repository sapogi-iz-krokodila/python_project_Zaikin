'''вывести первые N (N≥3) чисел Фибоначчи и посчитать количество четных чисел.'''

number = int(input("Введите N => 3 количество чисел "))

fib_prev = 1
fib_curr = 1
even_count = 0
i = 1


while i <= number:
    print(f"последовательность фибоначи: {fib_prev}")
    if fib_prev % 2 == 0:
        even_count += 1

    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next
    i += 1

print(f"четные числа фибоначи: {even_count}")