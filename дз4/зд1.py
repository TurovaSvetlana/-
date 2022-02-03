def simple_calc(x, y):
    pay = x * y
    c = pay/100*15
    #c-расчет премии
    return pay + c
x = float(input("введите число отработанных часов: "))
y = float(input('введите сумму оплаты труда за один час: '))
print(f'размер зароботной платы составил:{simple_calc(x, y)}')