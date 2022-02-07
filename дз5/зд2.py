# Создать текстовый файл(непрограммно),
# сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open('text.txt.py', 'r', encoding="utf-8") as file:
    my_list = file.readlines()
    for i in range(len(my_list)):
        new_l = my_list[i].split()
        print(f'Количество строк в файле {len(my_list)}.'
              f' В {i + 1}-ой строке {len(new_l)} слов(а)')






