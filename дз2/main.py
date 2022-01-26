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











