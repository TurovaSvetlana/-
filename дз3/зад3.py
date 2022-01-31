def mu_func(i1, i2, i3):
    a = [i1, i2, i3]
    a.sort()

    return a[1] + a[2]

print(mu_func(i1=8, i2=5, i3=3))