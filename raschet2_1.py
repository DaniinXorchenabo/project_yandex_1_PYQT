# -*- coding: utf8 -*-
from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt

print(113000*1.26)

g = 9.81# ускорение свободного падения на земле в м/с2.
rv = 1.29# плотность атмосферного воздуха в кг/м3.
rg = 0.17# плотность гелия в кг/м3.
R = 26# радиус оболочки стратостата в м.
b = 0.000125# константа, связанная с плотностью воздуха в 1/м
a = 6.5*10**-3# константа, связанная с температурой воздуха в К/м
c = 0.8# коэффициент лобового сопротивления
mo = 60# масса в кг
V = (4/3)*pi*R**3
print(V)
p2 = 3*c/(8*R)# введенный параметр
T0 = 300# температура на уровне моря
tz=4000# время зависания в секундах
rgu=1.2# плотность образовавшейся газовой смеси после  стравливания гелия в кг/м3 
tz=7000# время зависания
Vmin=500# начальный объём шара в/м3.
c=0.8#коэффициент лобового сопротивления
rs=rg+mo/Vmin# суммарная плотность материала стратостата, массы гелия и нагрузки
p1=rv/rs# введенный параметр
V = (4/3)*pi*R**3
print(V)
p2 = 3*c/(8*R)# введенный параметр
T0 = 300# температура на уровне моря
tz=4000# время зависания в секундах
rgu=1.2# плотность образовавшейся газовой смеси после  стравливания гелия в кг/м3 
tz=4000# время зависания
def fun(y, t):
    y1,y2= y
    if y2<=0:
        if t<tz:
            pass
    print([y2,((g*rv*exp(-b*y1)*V-mo-rg)-(rv*exp(-b*y1))/2*c*y2**2)], t)
            #return [y2,-g+g*(rv/(rgu+mo/V))*exp(-b*y1*T0/(T0-a*y1))+(rv/(rgu+mo/V))*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
            #return [y2,((2*(g*(rv*exp(-b*y1)*V-mo-rg)-2*y1))/(rv*exp(-b*y1)))*y2**2]
    #return [y2,0.5*((t**2*(g*rv*exp(-b*y1)*V-mo-rg)+(rv*exp(-b*y1))/2*c*y2**2)*t**2)]
    return [y2,((g*(rv*V*exp(-b*y1)-rs))-((rv*exp(-b*y1)*c)/2)*y2**2)]#
'''      
    return [y2,(g*(exp(-b*y1)*parametr1)-(exp(-b*y1)*parametr2)*y2)]#
parametr1 = (rv*V-mo-rg)
parametr2 = (rv*c)/2
'''
        #elif t>=tz:
           # return [y2,-g+g*(rv/(rgu+mo/V))*exp(-b*y1*T0/(T0-a*y1))+(rv/(rgu+mo/V))*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
    #else:
        #return [y2,-g+g*(rv/(rg+mo/V))*exp(-b*y1*T0/(T0-a*y1))-(rv/(rg+mo/V))*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
t =arange(0,tz+555,1)
y0 = [0,0]
[y1,y2]=odeint(fun, y0,t, full_output=False).T # full_output=False
plt.title("Подъём, зависание, спуск ЛАЛВ \n с жёсткой оболочкой сферической формы  \n Объём: %s м3. Масса : %s кг. Подъёмная сила: %s kН. "%(round(V,0),mo,round(0.001*g*rv*V,0)))
plt.plot(t,y1,label='Максимальная высота подъёма: %s км. \n Максимальная скорость: % s м/с .\n Время зависания %s с.'%(round(max(y1)/1000,2), round(max(y2),2),tz-2*555))
plt.ylabel('Высота в м')
plt.xlabel(' Время в сек.')
plt.legend(loc='best')
plt.grid(True)
plt.show()