# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

element_count = int(input("Ввести количество элементов списка"))
superlist = []
i = 0
el = 0
while i < element_count :
    superlist . append(input("Ввести значение списка"))
    i += 1

for  элемента  in range (int(len( superlist ) / 2 )):
        superlist [ el ], my_list [ el  +  1 ] = my_list [ el  +  1 ], my_list [ el ]
        el  +=  2
print ( superlist)