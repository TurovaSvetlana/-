s=[8,  56,  'Всем привет!', (6,7), {"5": "4"}]
for item in s:
    print(type(item))

s=[]
for g in range(9):
    a=input('введите значение;')
    s.append(a)
for i in range(len(s)):
    if i%2==0:
        if i != len(s)-1:
            s[i], s[i+1] = s[i+1],s[i]
print(s)


a=  input('введите номер месяца')
m={'зима': [12,1,2],
   'весна': [3,4,5],
   'лето': [6,7,8],
   'осень': [9,10,11]}
for f in m:
    if int(a) in m[f]:
        print(f)












# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
