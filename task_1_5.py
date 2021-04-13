#Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
import math
from fractions import Fraction

a = 5
b = 7

c = math.sqrt((a**2)+(b**2))
print(c)

i = Fraction(1, 2)
s = i * a * b #можно упростить -> s = ( a * b ) / 2
print(float(s)) #можно и int-овое если не важно значение после запятой