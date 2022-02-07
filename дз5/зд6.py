#Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий
# по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему.
# Вывести его на экран.

def count_subjects():
    True
        # Информатика: 100(л) 50(пр) 20(лаб).
    mydict = {}
    with open("file11.txt",'r+', encoding='utf-8') as fobj:
        for line in fobj:
            name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
            name_sum = sum(map(int, ''.join([i for i in stats if i == ' '
                            or ('0' <= i <= '9')]).split()))
            mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}

