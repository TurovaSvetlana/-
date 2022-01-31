def func(sum):
    a = input("введите числа")
    c = 0
    while a != '':
        t = a.split()
        for v in t:
            c = c + int(v)
print(func(sum))