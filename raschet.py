# -*- coding: utf8 -*-
from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt
g=9.81# ускорение свободного падения на земле в м/с2.
rv=1.29# плотность атмосферного воздуха в кг/м3.
rg=0.17# плотность гелия в кг/м3. 0,17
Vmin=500# начальный объём шара в/м3.
b=0.000128# константа, связанная с плотностью воздуха в 1/м.
c=0.8#коэффициент лобового сопротивления
mo=60#масса в кг
rs=rg+mo/Vmin# суммарная плотность материала стратостата, массы гелия и нагрузки
p1=rv/rs# введенный параметр
h=[(10**-3)*log((rv*w)/(mo+rg*Vmin))*b**-1 for w in arange(1*10**3,1.8*10**5,1000)]
print(max(h))
v=[(10**-3)*w for w in arange(1*10**3,1.8*10**5,1000)]
plt.title("Теоретическая зависимость высоты подъёма шара \n от его максимального объёма")
plt.plot(v,h)
plt.xlabel('Максимальный объём шара в тыс. м3')
plt.ylabel(' Максимальная высота подъёма в км.')
plt.grid(True)
plt.show()