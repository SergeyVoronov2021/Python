"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
"""

def simple_calc():
    x = float(input('Введите количество отработанных часов: '))
    y = float(input('Введите суммы оплаты труда за 1 час: '))
    c = float(input('Укажите размер премии: '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы: {simple_calc() }')
