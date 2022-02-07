# Создать текстовый файл(не программно).Построчно
# записать фамилии сотрудников и величину их окладов(не
# менее 10 строк).Определить, кто из сотрудников имеет
# оклад менее 20 тысяч, вывести фамилии этих сотрудников.Выполнить
# подсчёт средней величины дохода сотрудников.
def workers_statistics():
    with open('nev_text.txt', 'r+', encoding="utf-8") as file:
        l = file.readlines()
        poor = []
        sum = 0
        for i in range(len(l)):
            ol = l[i].split()
            salary = float(ol[2])
            if salary < 20000:
                poor.append(ol[0])
            sum = sum + salary

        print(f'Средняя величина дохода сотрудников равна '
            f'{sum / len(l):.2f}')
        print(f'меньше 20000 получает сотрудник:{", ".join(poor)}')


workers_statistics()