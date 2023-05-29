from Iteracion import Iteracion

h = 0.01
Pn = 800
t = 0.01

while t <= 5:
    i = Iteracion(t)
    i.calcular(h, Pn)
    print(f'\n{i}')
    Pn = i.P
    t += h
