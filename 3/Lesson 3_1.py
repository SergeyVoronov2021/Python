"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def exe_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    except ValueError:
        return 'Ошибка'

def exe_1_use():
    print(exe_1((int(input('Ввести первое числоr: '))), (int(input('Ввести второе число: ')))))