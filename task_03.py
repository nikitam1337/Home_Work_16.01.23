# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

number_A = int(input('Введите A: '))
number_B = int(input('Введите B: '))

def exponentiation (a,b):
    if b==1:
        return a
    else:
        return a*exponentiation(a,b-1)
result = exponentiation(number_A, number_B)
print(result)
