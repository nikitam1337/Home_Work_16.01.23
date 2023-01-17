# Задача 31: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
##############################

# Решение 1-м способом:

# start_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# min_element = int(input('Введите нижнюю границу диапазона: '))
# max_element = int(input('Введите верхнюю границу диапазона: '))
# result=[]
# for i in range(len(start_list)):
#     if min_element<=start_list[i]<=max_element:
#         result.append(i)

# print (result)

# Решение 2-м способом: 
start_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_element = int(input('Введите нижнюю границу диапазона: '))
max_element = int(input('Введите верхнюю границу диапазона: '))
result=[i for i in range(len(start_list)) if min_element<=start_list[i]<=max_element]
print (result)

# ИЛИ:  28+29 строки в одной:
# print ([i for i in range(len(start_list)) if min_element<=start_list[i]<=max_element])
