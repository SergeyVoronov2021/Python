"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

#Возврат прописной первой буквы
def my_title(word):
    return word[:1].upper() + word[1:].lower()

print(my_title('apocalyptica'))

# Разделение слов в строке пробелом
def my_title(*word):
    for w in word:
        result = []
        for word in w.split():
            result.append(word[:1].upper() + word[1:].lower())
    return ' '.join(result)
print(my_title('iron maiden, def leppard, black sabbath, deep purple'))






