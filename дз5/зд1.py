 # Создать программный файл в текстовом формате,
 # записать в него построчно данные, вводимые пользователем.
 # Об окончании ввода данных будет свидетельствовать пустая строка.


with open('new_file.txt', 'w') as file:
    while True:
        user_answ = input('введите текст: ')
        file.write(user_answ + '\n')
        if not user_answ:
            break
