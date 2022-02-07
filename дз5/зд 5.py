def rewrite_file():
    with open('filsse.txt', 'w+') as file:
        file.write(input('Введите числа через пробел: '))
    with open('filsse.txt', 'r') as file:
        l = map(int, file.read().split())
        print(sum(l))
rewrite_file()

