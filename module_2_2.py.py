first = int(input('Введите любое число от 1 до 10: '))
second = int(input('Введите любое число от 1 до 10: '))
third = int(input('Введите любое число от 1 до 10: '))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')