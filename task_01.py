# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element = int(input('Введите первый элемент последовательности: '))
step = int(input('Введите шаг арифметической прогрессии: '))
volume = int(input('Введите кол-во элементов арифметической прогрессии: '))

def formula (n):
    element = first_element+(n-1)*step
    return element

result = [formula(i) for i in range(1,volume+1)]
print(result)