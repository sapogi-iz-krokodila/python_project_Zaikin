'''Дано целое число. Если оно является положительным, то прибавить к нему 20, в
противном случае вычесть из него 5.'''

number_a = int(input("Введите целое число "))
if number_a > 0:
    increase = number_a + 20
    print(f"{increase}")
else:
    decrease = number_a - 5
    print(f"{decrease}")