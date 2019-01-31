# -*- coding: utf8 -*-
from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt
g=9.81# ускорение свободного падения на земле в м/с2.
rv=1.29# плотнеть атмосферного воздуха в кг/м3.
rg=0.17# плотность гелия в кг/м3.
R=110# радиус оболочки стратостата в м.
b=0.000125# константа, связанная с плотностью воздуха в 1/м
a=6.5*10**-3# константа, связанная с температурой воздуха в К/м
c=0.4#коэффициент лобового сопротивления
mo=40#масса в кг
V=(4/3)*pi*R**3
rs=rg+mo/V# суммарная плотность материала стратостата, массы гелия и нагрузки
p1=rv/rs# введенный параметр
p2=3*c/(8*R)# введенный параметр
T0=300
def fun(y, t):
         w, y2= y    
         return [y2,-g+g*p1*exp(-b*y1*T0/(T0-a*y1))-p1*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
#  for w in arange(1*10**3,1.8*10**6,5000)
t =arange(0,2600,0.01)
y0 = [0.0,0.0]
[y1,y2]=odeint(fun, y0,t, full_output=False).T
plt.figure()
plt.title("Скорость подъёма стратостата  \n Объём: %s м3. Масса : %s кг"%(round(V,0),mo))
plt.plot(t,y2,label="Максимальная скорость подъёма %s м/с"%round(max(y2),1))
plt.xlabel('Время в c')
plt.ylabel(' Скорость в м/с')
plt.legend(loc='best')
plt.grid(True)
plt.figure()
plt.title("Высота подъёма стратостата \n Объём: %s м3. Масса : %s кг"%(round(V,0),mo))
plt.plot(t,y1,label='Максимальная высота подъёма: %s км'%round(max(y1)/1000,2))
plt.ylabel('Высота в м')
plt.xlabel(' Время в c')
plt.legend(loc='best')
plt.grid(True)
plt.show()