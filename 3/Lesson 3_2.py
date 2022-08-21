"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
name = input('Ввести имя')
surname = input('Ввести фамилию')
year = int(input('Ввести год рождения'))
city = input('Ввести страну')
email = input('Ввести адрес электронной почты')
telephone = input('Ввести контактный телефон')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Till', name = 'Lindemann', year = '1984', city = 'Hamburg', email = 'rammstein@gmail.com', telephone = '8-123-456-78-90'))