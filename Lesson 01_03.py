#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Ввеcти число - '))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
total = n + int(t1) + int(t2)
print(total)