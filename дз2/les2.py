a=  input('введите номер месяца')
m={'зима': [12,1,2],
   'весна': [3,4,5],
   'лето': [6,7,8],
   'осень': [9,10,11]}
for f in m:
    if int(a) in m[f]:
        print(f)