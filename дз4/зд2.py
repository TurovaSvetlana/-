list = [18,28,45,154,78,2,0,45,64]
nev_list = [number for i,number in enumerate(list)if i>0 and list[i]>list[i-1]]
print(nev_list)