# Дано целое число $N (> 0)$. Найти сумму $1 + 1/2 + 1/3 + \dots + 1/N$
while True:
    try:
        n = int(input("Введите число больше 0: "))
        if n >= 0:
            break
        else:
            print("Ошибка число должно быть больше 0:")
    except ValueError:
        print("Введите корректное значение")

total_sum = 0.0
i = 1


while i <= n:
    total_sum += 1 / i
    i += 1
    
print(total_sum)