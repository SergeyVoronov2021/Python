# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


superlist = [7, 'Naturlich, das ist sehr schwer fuer mich', 13, 'Metallica', None, 0.5]

def my_type(el):
    for el in range(len(superlist)):
        print(type(superlist[el]))
    return
my_type(superlist)







